# bridgeobjects
A collection of modules that allows the user to utilise objects used in bridge games, for example, a board or a contract.

The classes form a natural hierarchy:

 event
    └── board
        ├── auction
        │   └── call
        │       └── denomination
        ├── contract
        ├── hand
        │   └── card
        │       └── suit
        └── trick

(However, some classes are natural subsidiaries not represented in this classification, for example, there are four cards in a trick.)


The objects can be created using a simple, self explanatory, human readable set of definitions
by using Portable Bridge Notation (PBN) (http://www.tistis.nl/pbn/) or
Richard’s Bridge Notation (RBN) (http://www.rpbridge.net/7a12.htm).

## Installation
```bash
pip install bridgeobjects
```
