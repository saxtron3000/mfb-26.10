"""Reopen a reference when final audit finds a missed visible restriction."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import reference_batch as b

aid, reason = sys.argv[1:3]
state = json.loads(b.STATE.read_text())
item = next(i for i in state['items'] if i['assetId'] == aid)
assert item['status'] == 'completed'
assert not any(i['status'] == 'generating' for i in state['items'])
review = Path(item['expectedFiles']['json'].replace('-ref.json', '-review.json'))
number = len(item.get('rejections', [])) + 1
archive = b.ROOT / 'Assets/rejected' / (aid.lower() + '-attempt-' + str(number).zfill(2) + '-prior-acceptance.json')
shutil.copy2(review, archive)
item.setdefault('rejectedFiles', []).append(str(archive))
item.setdefault('finalAuditCorrections', []).append(reason)
checklist_path = b.ROOT / 'workspace/24_codex-reference-image-prompt-checklist.md'
checklist = checklist_path.read_text()
before = '### [X] ' + aid + ' —'
assert checklist.count(before) == 1
checklist_path.write_text(checklist.replace(before, before.replace('[X]', '[ ]'), 1))
state['sourceRevision']['sha256'][str(checklist_path)] = hashlib.sha256(checklist_path.read_bytes()).hexdigest()
item['checklistMark'] = ' '
item['status'] = 'generating'
# It is the same image already counted at first review, not a new image.
state['reviewedImages'] -= 1
b.reject(state, item, reason)
print(json.dumps({'assetId': aid, 'status': item['status'], 'editSource': str(archive).replace('-prior-acceptance.json', '.png')}))
