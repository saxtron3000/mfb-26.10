"""Local reference-queue records only; never creates production assets."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
REFS = ROOT / 'Assets/references'
STATE = REFS / 'reference-batch-state.json'
LOG = REFS / 'reference-batch-completion-log.jsonl'


def now():
    return datetime.now(timezone.utc).isoformat()


def write_json(path, value):
    path = Path(path)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temp.replace(path)


def source_data(aid):
    index = (ROOT / 'workspace/08_assets.md').read_text()
    checklist = (ROOT / 'workspace/24_codex-reference-image-prompt-checklist.md').read_text()
    match = re.search(r'^### \[([ Xx])\] ' + aid + r' — \w+\n\n```text\n(.*?)\n```', checklist, re.M | re.S)
    assert match, aid
    row = next(line for line in index.splitlines() if line.startswith('| `' + aid + '` |') and len(line.strip('|').split('|')) == 11)
    cells = [v.strip() for v in row.strip('|').split('|')]
    registry = index.split('### Complete reference classification registry\n', 1)[1].split('\n## 8.', 1)[0].strip()
    shared = index.split('## 2. Shared design requirements\n', 1)[1].split('\n## 3.', 1)[0].strip()
    register = index.split('## 8. Shared actor, prop and interface register\n', 1)[1]
    components = '\n'.join(m[0].strip() for m in re.finditer(r'^- id: .*?(?=^- id: |\n```|\Z)', register, re.M | re.S) if aid in m[0])
    legacy_match = re.search(r'```yaml\nid: ' + aid + r'\n.*?\n```', index, re.S)
    legacy = legacy_match[0] if legacy_match else ''
    return match[2], row, cells, registry, shared, components, legacy


def report(state):
    state['totals'] = {name: sum(i['status'] == name for i in state['items']) for name in ['completed', 'deferred', 'blocked', 'pending', 'generating']}
    lines = ['# Reference-image batch report', '', 'Reference generation only. No production assets have been published.', '',
             '101 indexed items; current states: ' + ', '.join(str(n) + ' ' + k for k, n in state['totals'].items()) + '.', '',
             'Output contract: transparent PNG reference and white-background JPG preview of the same composition and dimensions, plus JSON conformance report and exact prompt record.', '',
             '| Order | Asset | State | Created files |', '|---|---|---|---|']
    for item in state['items']:
        links = ', '.join('[' + Path(p).name + '](' + str(Path(p).relative_to(REFS.parent)).replace('prompts/', '../prompts/').replace('references/', '') + ')' for p in item['createdFiles']) or '—'
        lines.append('| ' + str(item['queuePosition']) + ' | ' + item['assetId'] + ' | ' + item['status'] + ' | ' + links + ' |')
    lines += ['', '## Unresolved', '']
    for item in state['items']:
        lines.extend('- ' + item['assetId'] + ': ' + reason for reason in item['unresolved'])
    lines += ['', '## All created file paths', '']
    paths = sorted(str(p.resolve()) for p in (ROOT / 'Assets').rglob('*') if p.is_file() and p.suffix not in ['.env', '.pyc'])
    lines += ['This inventory includes accepted references, review records, prompts, queue utilities, rejected attempts, and the preserved superseded run. All are local working files.', '', str(len(paths)) + ' file paths:', '']
    lines.extend('- `' + p + '`' for p in paths)
    lines += ['', 'Prior blocked records and unsubmitted prompts are archived at `' + state['previousRunArchive'] + '`.', '', '## Validation and handoff limits', '',
              '- The corrected contract covers 101 indexed items, not the original stated 99: 98 eligible; BD-V-001, BD-V-070 and BD-V-075 deferred.',
              '- Each completed item has a transparent PNG, same-size white-background JPG, six-root-key JSON conformance report, exact completed prompt record, and separate visual review record.',
              '- The reference batch contains 392 required deliverables and 98 accepted visual review records. Every accepted image was visually reviewed; rejected attempts are retained separately.',
              '- File audit: [reference-batch-audit.json](reference-batch-audit.json). It verifies actual image decoding, transparency, matching dimensions, white preview corners, sampled composition agreement, JSON schema, complete brief inclusion, exact-prompt hashes, source hashes, checklist marks and all 101 dispositions.',
              '- All accepted references are 768 pixels wide. Resolution, aspect ratio, actual export settings, placements and review notes are recorded per asset.',
              '- Tool: image_gen.imagegen. Its model identifier and generation seed/quality settings are not exposed; model is recorded as null rather than invented.',
              '- Final audit corrected prohibited bubbles in BD-V-084, BD-V-088 and BD-V-089. Earlier accepted versions are archived and superseded.',
              '- BD-V-076 was revisited after the main queue: a blank structural download-panel reference resolves its earlier interpretation blocker. The final report retains only its production verification requirement.',
              '- Structural payment/link panels contain no QR, destination text or payment instructions. TODO AST-001, AST-002 and AST-003 remain unresolved for production.',
              '- References and all working records remain in ignored Assets/. No production code, manuscript insertion, Sanity upload or publication was performed.',
              '- Generation calls: ' + str(state['generationCalls']) + '; distinct generated images reviewed: ' + str(state['reviewedImages']) + '. One BD-V-077 tool call failed on an inaccessible edit-source path and returned no image; the retry used its workspace copy.', '']
    if state.get('finalValidation'):
        lines += ['Final validation: ' + state['finalValidation'], '']
    (REFS / 'reference-batch-report.md').write_text('\n'.join(lines))
    state['lastUpdatedAt'] = now()
    write_json(STATE, state)


def event(state, item, name):
    item['lastUpdatedAt'] = now()
    with LOG.open('a') as f:
        f.write(json.dumps({'event': name, 'recordedAt': now(), 'assetId': item['assetId'], 'status': item['status'], 'createdFiles': item['createdFiles'], 'unresolved': item['unresolved']}, ensure_ascii=False) + '\n')
    report(state)


def update_prompt(item, changes):
    path = Path(item['expectedFiles']['prompt'])
    title, rest = path.read_text().split('\n\n', 1)
    metadata, prompt = rest.split('\n\n===== EXACT ASSEMBLED PROMPT =====\n', 1)
    metadata = json.loads(metadata)
    metadata.update(changes)
    path.write_text(title + '\n\n' + json.dumps(metadata, ensure_ascii=False, indent=2) + '\n\n===== EXACT ASSEMBLED PROMPT =====\n' + prompt)


def submitted(state, item):
    assert item['status'] == 'generating'
    item['generationAttempted'] = True
    state['generationCalls'] += 1
    update_prompt(item, {'status': 'submitted', 'promptSubmitted': True, 'attemptStartedAt': now()})
    event(state, item, 'generation_submitted')


def finish(state, item, review_path):
    review = json.loads(Path(review_path).read_text())
    assert item['status'] == 'generating' and review['accepted'] is True
    assert Path(item['expectedFiles']['png']).read_bytes().startswith(b'\x89PNG\r\n\x1a\n')
    assert Path(item['expectedFiles']['jpg']).read_bytes().startswith(b'\xff\xd8')
    export = review['export']
    assert all(export[k] for k in ['pngTransparencyVerified', 'jpgWhiteBackgroundVerified', 'exportsMatch'])
    data = json.loads(Path(item['expectedFiles']['json']).read_text())
    data['canvas'].update(review['canvas'])
    data['placement'] = review['placement']
    data['conformance'].update(review['conformance'])
    data['conformance'].update({'reviewStatus': 'passed', 'imageGenerated': True, 'visualReviewPerformed': True, 'pngTransparencyVerified': True, 'jpgWhiteBackgroundVerified': True, 'exportsMatch': True, 'exportVerification': export, 'reviewNote': review['reviewNote']})
    data['unresolved'].extend(review.get('unresolved', []))
    assert data['conformance']['compositionFollowed'] and not data['conformance']['textPresentInImage']
    assert not data['conformance']['mustNotViolations']
    write_json(item['expectedFiles']['json'], data)
    update_prompt(item, {'status': 'passed', 'promptSubmitted': True, 'generationDate': review['generationDate'], 'tool': 'image_gen.imagegen', 'model': review.get('model'), 'generatorOutputHint': review['outputHint'], 'exportSettingsAndChecks': export, 'reviewNote': review['reviewNote'], 'unresolved': data['unresolved']})
    item['createdFiles'] = list(item['expectedFiles'].values())
    update_prompt(item, {'toolInput': review.get('toolInput', {})})
    assert all(Path(p).exists() for p in item['createdFiles'])
    item['createdFiles'].append(str(Path(review_path).resolve()))
    path = ROOT / 'workspace/24_codex-reference-image-prompt-checklist.md'
    checklist = path.read_text()
    before = '### [ ] ' + item['assetId'] + ' —'
    assert checklist.count(before) == 1
    path.write_text(checklist.replace(before, before.replace('[ ]', '[X]'), 1))
    state['sourceRevision']['sha256'][str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
    item['status'] = 'completed'
    item['checklistMark'] = 'X'
    item['generationAttempted'] = True
    item['visualReviewPerformed'] = True
    item['unresolved'] = data['unresolved']
    state['reviewedImages'] += 1
    event(state, item, 'review_passed_and_checklist_marked')


def block(state, item, reason):
    assert item['status'] == 'generating'
    data = json.loads(Path(item['expectedFiles']['json']).read_text())
    data['unresolved'].append(reason)
    data['conformance']['reviewStatus'] = 'blocked'
    data['conformance']['compositionDeviation'] = reason
    write_json(item['expectedFiles']['json'], data)
    update_prompt(item, {'status': 'blocked', 'reviewNote': reason, 'unresolved': data['unresolved']})
    item['status'] = 'blocked'
    item['unresolved'] = data['unresolved']
    event(state, item, 'blocked')


def reject(state, item, reason):
    assert item['status'] == 'generating'
    number = len(item.get('rejections', [])) + 1
    prefix = ROOT / 'Assets/rejected' / (item['assetId'].lower() + '-attempt-' + str(number).zfill(2))
    import shutil
    saved = []
    for kind, source in item['expectedFiles'].items():
        source = Path(source)
        if source.exists():
            destination = Path(str(prefix) + source.suffix)
            shutil.copy2(source, destination)
            saved.append(str(destination))
            if kind in ['png', 'jpg']:
                source.unlink()
    review_path = Path(str(prefix) + '-review.json')
    write_json(review_path, {'assetId': item['assetId'], 'attempt': number, 'status': 'rejected', 'reviewedAt': now(), 'reason': reason, 'files': saved})
    saved.append(str(review_path))
    item.setdefault('rejectedFiles', []).extend(saved)
    item.setdefault('rejections', []).append(reason)
    item['status'] = 'pending'
    state['reviewedImages'] += 1
    event(state, item, 'reference_rejected')


def prepare(state, item, direction):
    aid = item['assetId']
    assert item['status'] in ['pending', 'blocked'], item['status']
    assert not any(i['status'] == 'generating' for i in state['items'])
    for path, digest in state['sourceRevision']['sha256'].items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest, 'Source changed: ' + path
    checklist, row, cells, registry, shared, components, legacy = source_data(aid)
    adjacent = ''
    anchor = re.search(r'`(#{2,4} [^`]+)`', cells[6])
    guide_name = 'mfb-bd-eg-26.10.md' if cells[6].startswith('EG only:') else 'mfb-bd-sg-26.10.md'
    guide_path = ROOT / 'publish/mfb-bd-26.10' / guide_name
    if anchor and guide_path.exists():
        guide = guide_path.read_text()
        found = re.search(r'^' + re.escape(anchor[1]) + r'\s*$', guide, re.M)
        if found:
            tail = guide[found.end():]
            following = re.search(r'^#{1,6} ', tail, re.M)
            adjacent = guide[found.start():found.end()] + tail[:following.start() if following else len(tail)]
    contract = (ROOT / 'workspace/22_openai-reference-image-prompt.md').read_text()
    specification = registry + '\n\nComplete incorporated section 3 entry:\n' + row + '\n\nShared section 2 requirements:\n' + shared
    if legacy:
        specification += '\n\nExisting structural record, subject to registry version 3:\n' + legacy
    for before, after in {'[BD-V-000]': aid, '[paste specification]': specification, '[paste entry]': row, '[paste entries, if any]': components or 'No section 8 entry explicitly lists this asset.', '[paste only when it clarifies the lesson]': adjacent or 'No adjacent guide text supplied. Do not invent strings or values.', '[asset-id-lowercase]': aid.lower(), 'bd-v-000': aid.lower(), '"BD-V-000"': '"' + aid + '"'}.items():
        contract = contract.replace(before, after)
    prompt = ('Create exactly ONE image for ' + aid + '. Return the transparent PNG; its JPG preview is a local export from that same composition. '
              'STRICT PIXEL RESTRICTIONS: no letters, numerals, pseudo-writing, placeholder text strokes, page writing, logos, QR patterns, arrows, connectors, frames, borders, decorative rays, sparkles, stars, floating marks, or unrelated icons. '
              'All book pages and screens must be unmarked. Flat opaque fills only, no gradients, shading, highlights, shadows, texture, or grain. Front-facing orthographic forms without perspective or depth. Only the specified instructional objects, with transparent empty space around them.\n\n'
              + 'COMPLETE CHECKLIST PROMPT\n' + checklist + '\n\nCOMPLETED SHARED CONTRACT\n' + contract
              + '\n\nBINDING VISUAL STYLE\n' + (ROOT / 'workspace/27_assets-style.md').read_text()
              + '\n\nASSET-SPECIFIC COMPOSITION FOR THIS ATTEMPT\n' + direction)
    unresolved = []
    todos = {'BD-V-036': 'AST-001', 'BD-V-078': 'AST-002', 'BD-V-080': 'AST-003'}
    if aid in todos:
        unresolved.append('TODO ' + todos[aid] + ': production payment values remain [BLANK]; structural reference only, no QR or real payment destination. Preserve every approval and validation requirement in the complete brief.')
    data = {'assetId': aid, 'specVersion': 3, 'canvas': {'aspectRatio': '', 'orientation': 'landscape', 'suggestedWidthPx': 1024, 'reference': {'fileName': aid.lower() + '-ref.png', 'format': 'PNG', 'background': 'transparent'}, 'preview': {'fileName': aid.lower() + '-ref.jpg', 'format': 'JPEG', 'background': '#FFFFFF'}}, 'placement': [],
            'conformance': {'elementsRendered': [], 'elementsMissing': ['Not generated or reviewed yet.'], 'elementsAdded': [], 'compositionFollowed': False, 'compositionDeviation': 'Generation and visual review pending.', 'countDeviations': [], 'mustNotViolations': [], 'textPresentInImage': [], 'shapeBudgetEstimate': 0, 'pngTransparencyVerified': False, 'jpgWhiteBackgroundVerified': False, 'exportsMatch': False,
                            'reviewStatus': 'pending', 'imageGenerated': False, 'visualReviewPerformed': False,
                            'deferredForEditableCoding': {'completeSourceBrief': row, 'sourcePlacement': cells[6], 'sourceLocator': cells[7], 'instructionalRelationship': cells[8], 'allRequiredTextConnectorsAndPlacementInstructions': cells[9], 'format': cells[10], 'existingStructuralRecord': legacy, 'relevantSharedRegister': components}}, 'unresolved': unresolved}
    metadata = {'assetId': aid, 'status': 'prepared', 'preparedAt': now(), 'generationDate': None, 'tool': 'image_gen.imagegen', 'model': None, 'sourceBriefRevision': state['sourceRevision'], 'settings': {'requestedFormat': 'PNG', 'requestedBackground': 'transparent', 'requestedResolution': 'low', 'previewFormat': 'JPEG', 'previewBackground': '#FFFFFF', 'sameDimensions': True}, 'promptSubmitted': False, 'promptSha256': hashlib.sha256(prompt.encode()).hexdigest(), 'reviewNote': 'Generation and review pending.', 'unresolved': unresolved}
    if adjacent:
        data['conformance']['deferredForEditableCoding']['adjacentGuideText'] = adjacent
        metadata['adjacentGuideSource'] = {'path': str(guide_path), 'heading': anchor[1], 'excerptSha256': hashlib.sha256(adjacent.encode()).hexdigest()}
    record = 'REFERENCE PROMPT RECORD\n\n' + json.dumps(metadata, ensure_ascii=False, indent=2) + '\n\n===== EXACT ASSEMBLED PROMPT =====\n' + prompt + '\n===== END EXACT ASSEMBLED PROMPT =====\n'
    Path(item['expectedFiles']['prompt']).write_text(record)
    write_json(item['expectedFiles']['json'], data)
    item['createdFiles'] = [item['expectedFiles']['json'], item['expectedFiles']['prompt']]
    item['unresolved'] = unresolved
    item['status'] = 'generating'
    event(state, item, 'prompt_prepared')
    return {'assetId': aid, 'prompt': prompt, 'paths': item['expectedFiles']}


if __name__ == '__main__':
    state = json.loads(STATE.read_text())
    action = sys.argv[1]
    if action == 'report':
        report(state)
        print(json.dumps(state['totals']))
    elif action == 'prepare':
        item = next(i for i in state['items'] if i['assetId'] == sys.argv[2])
        print(json.dumps(prepare(state, item, sys.argv[3]), ensure_ascii=False))
    elif action in ['submitted', 'finish', 'block', 'reject']:
        item = next(i for i in state['items'] if i['assetId'] == sys.argv[2])
        if action == 'submitted':
            submitted(state, item)
        elif action == 'finish':
            finish(state, item, sys.argv[3])
        elif action == 'block':
            block(state, item, sys.argv[3])
        else:
            reject(state, item, sys.argv[3])
        print(json.dumps({'assetId': item['assetId'], 'status': item['status'], 'totals': state['totals']}))
    else:
        raise SystemExit('Unknown action')
