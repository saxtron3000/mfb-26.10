# Activity Title: Exploring the Mempool

## Keywords

**Bitcoin** **Tools**

## Activity Type

## Participation

## Duration

**30 minutes**

## Description

Students use mempool.space to inspect recent blocks, transactions, fees, inputs, outputs, and block rewards. The activity introduces the difference between a node’s mempool and a block explorer, uses block-height examples to discuss halvings and epochs, and optionally explores block art and other network data.

## Objectives

- Learners practice using a block explorer to find and interpret basic information about a Bitcoin block or transaction.

## Preparation

### Materials

• You will need a screen and access to the internet so you can project mempool.space for the entire class to watch and use together.

• Alternatively, you can direct students to access mempool.space on their personal phones or computers.

### Preparation Notes

Familiarize yourself with mempool.space. Ensure you can answer all the activity questions. For bonus discussions, explore the other sections of mempool.space (e.g., “mempool goggles,” diﬃculty adjustment, hashrate, Lightning, etc.)

Another idea for bonus discussions is to find special blocks.

Several examples are listed in this guide. It is important to test these before class because you may need to adjust settings within mempool.space, like toggling to “audit” view.

## Procedure

### Setup

If you are projecting using a screen, connect your device.

Navigate to mempool.space and ensure it is displaying properly.

If students are using their own phones or computers, they can go to https://mempool.space/ or scan this QR.

### Overview

In this activity you walk students through basic Bitcoin information available at mempool.space.

Time permitting, you can show them other tools available, like the mining or Lightning features.

Artistic blocks are a way to make the discussion more interesting for your non-technical students. A few options are included in this guide.

### Step 1: Introduction to the Dashboard

Mempool.space has added many features since it was first created.

The first thing you see at the top of the site, the blocks, is arguably the most critical to understand.

Ask questions to start the overview:

• “What’s the diﬀerence between the green and purple blocks?”
• “What was the last block mined?”
• “How many transactions were in the block?”
• “How long ago was it added to the timechain?”
• “Who mined it?”

### Step 2: Diving Deeper: Blockchain (All Blocks), One Block

Explain to students that by clicking on a block you can explore more details.

When you do this, students can see details, such as transaction fees paid to the miner, on the left-hand side.

On the right side is the block visualizer, which gives a sense of how much “space” each transaction takes up within the 4 MB block limit. Larger cubes mean bigger transactions.

Quick breakdown:

• **Cubes = Transactions:** Each cube is one transaction, arranged in a grid based on its order in the block (the x-y plane shows the sequence and packing).

• **Height = Size in vB:** Taller cubes = larger transactions, e.g., those with many inputs/outputs.

• **Color = Fee Rate:** Blues/greens = low fees, e.g., <1 sat/vB; yellows/oranges = medium, reds = high fees, e.g., >10+ sat/vB.

• **Other Dimensions:** Width/depth might be normalized or fixed for the grid, but height scales directly with vB to show relative sizes.

### Step 3: Going Deeper: One Block (Many Transactions), One Transaction

Explain to students that by clicking on a transaction you can explore more details. If you have a specific transaction, you can also use the search tool.

The example below is block 800,000.

You can further drill down by selecting a specific input, or specific output.

Questions for discussion:

• What is significant about block 800,000? (Trick question… it is not a halving! One epoch = 210,000 blocks.)
• How does this diagram of inputs and outputs relate to UTXOs?
• Why might someone overpay a transaction fee?

Remind students that a halving occurs every 210,000 blocks. A group of 210,000 blocks is also called an epoch.

The fourth halving occurred at block 840,000.

Go to the search tool and type “840000”.

Questions:

• Why would this block have so many high transaction fees?
• What was the total block reward (subsidy + transaction fees) paid to the miner?

### Step 4: Optional: Mempool Art

This section adds some fun to learning the tool.

Miners can intentionally arrange transactions by their fee rates and/or sizes to form visual patterns using mempool.space’s visualization tool.

You can navigate to these blocks by putting the block height in the search tool or by following the links.

**Block Height: 836361** **Miner: MARA Pool** **Date: 26-Mar-24**

https://mempool.space/block/836361

A large, bold letter "M" (for Marathon) formed by clustering low-fee transactions into a pixelated shape across the block's transaction grid. This was one of the first high-profile examples of intentional block art.

**Block Height: 879613** **Miner: MARA Pool** **Date: 17-Jan-25**

https://mempool.space/block/879613

A pixelated portrait of Donald Trump (labeled "Trump 47"), created by precise transaction ordering. It cost over 1.2 BTC in fees to curate, highlighting the economic creativity in Bitcoin mining.

**Block Height: 880512** **Miner: SEC Pool** **Date: 24-Jan-25**

https://mempool.space/block/880512

A stylized image of Satoshi Nakamoto's photo alongside the Genesis Block declaration ("The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"). Includes OP_RETURN messages emphasizing Bitcoin's origins; the pattern uses transaction clusters for contrast.

**Note, you may have to adjust some of mempool.space’s settings to see the images clearly.**

**First try toggling the “Audit” button.**

**If this does not work, consider asking a technical Bitcoiner or using an AI tool to troubleshoot.**

**AFTER toggling “Audit” view**

**BEFORE toggling “Audit” view**

### Step 5: Optional: Exploring Other Areas

There are other tools that relate to earlier subjects: e.g., Lightning, mining, hashrate, diﬃculty adjustment, UTXO visualization, and others.

### Step 6: Discussion

Wrap up the activity with a class discussion.

## Review

### Key Points

1. **“Mempool” refers to a list of unconfirmed transactions maintained by each Bitcoin node, not a specific service or platform.**
2. There is no single, universal mempool. Mempool.space is one of many.
3. Mempool.space is open-sourced and well known for being an easy-to-use visual block explorer. It provides real-time data on unconfirmed transactions, fee rates, and other network activity.

### Discussion questions

• Is there only one mempool?
• Who manages mempools?
• Can you have your own mempool?

Yes! When you run your own full Bitcoin node, you have a memory pool of unconfirmed transactions that the node has received, validated, and is holding until they are included in a block by miners. This is a core part of how nodes contribute to Bitcoin's decentralization and security.

Some companies can and do have their own mempools too, e.g., MARA or Braiins.

There are other mempools available for those who do not run a node, e.g., https://blockstream.info

• What are potential benefits of having your own node?

**Hint:** “Don’t trust. Verify.”

## Notes

**Diploma assessment link:** May provide the individual-response context for [`T3` / `C8`](https://programs.myfirstbitcoin.org/programs/educator-guide/), especially on-chain confirmation and verification. Use the approved protocol and record individual evidence; otherwise, this activity is formative.

This activity takes about 30 minutes for a typical class.

Because mempool.space has added new tools and views, there are many ways to extend the class by diving deep into the details.

Conversely, you can shorten the duration of the activity by skipping those extra features.

## Additional Resources

**“How to explore the Bitcoin Blockchain Mempool.space Tutorial”** on the YouTube channel Crypto Trading Guides covers transaction fees, diﬃculty adjustment, checking addresses, checking transactions.

https://youtu.be/ZQZJI0R79sM?si=FkZf8WiH2xVvsBi4
