# newrl
This library contains wrapper functions for interacting with the Newrl blockchain. Off chain and on chain operations are available.

## Installation
Add `newrl` to your project requirements 
and/or run the installation with:
```shell
pip install newrl
```


## Usage

### Initialise a node connection
A node address along with port can be given to initialise a new node connection. If no address is provided, the default newrl foundation node at address `http://newrl.net:8090` will be used.

```python
node = Node('http://3.6.236.206:8090')
```

### Off chain operations
#### Get file hash
Certain Newrl operations use document hashes for verification purpose. A file hash can be obtained with the below command.

```python
from newrl import get_file_hash

file_hash = get_file_hash('/Users/admin/Documents/Tokenisation_Agreement1.pdf')
print(file_hash)
```

#### Generate new wallet
A wallet address generation can be done off-chain. The result is a dictionary containing public, private and address of the new wallet. A wallet once generated should be added to the chain to make it available for use.

```python
from newrl import generate_wallet_address

wallet = generate_wallet_address()
```

#### Sign transaction
A transaction need to be signed with the applicable wallet for addition to chain.
```python
from newrl import sign_transaction

signed_wallet_add_transaction = sign_transaction(wallet, wallet_add_transaction)
print(signed_wallet_add_transaction)
```

### On chain operations
#### Add wallet to chain
A wallet address once genearated need to be signed and then added to the chain.
```python
def add_wallet(
    custodian_address: str,
    jurisdiction: str,
    public_key: str,
    ownertype: str = '1',
    kyc_docs: list = [],
    specific_data: dict = {},
)
```
Example
```python
wallet_add_transaction = node.add_wallet(
    wallet['address'], '910', wallet['public'], 1)

print(wallet_add_transaction)
```

#### Add token to chain
A token can be created, signed and then validated to add to the chain.
```python
def add_token(
        token_name: str,
        token_type: str,
        first_owner: str,
        custodian: str,
        legal_doc_hash: str,
        amount_created: int,
        value_created: int,
        disallowed_regions: list = [],
        token_attributes: dict = {},
        is_smart_contract_token: bool = False,
    )
```
Example
```python
    token_add_transaction = node.add_token(
        'my_new_token',
        '1',
        '0x16031ef543619a8569f0d7c3e73feb66114bf6a0',
        '0x16031ef543619a8569f0d7c3e73feb66114bf6a0',
        'fhdkfhldkhf',
        10000,
        10000,
    )
```

#### Add transfer
A transfer can be created between two wallets either unilaterally or bilaterally depending on the transfer type.
```python
def add_transfer(
        self,
        asset1_code: int,
        asset2_code: int,
        wallet1_address: str,
        wallet2_address: str,
        asset1_qty: int,
        asset2_qty: int,
        transfer_type: int = 4,
    )
```
Example
```python
    transfer_transaction = node.add_transfer(
        9, 10, '0x16031ef543619a8569f0d7c3e73feb66114bf6a0', '0x16031ef543619a8569f0d7c3e73feb66114bf6a0', 10, 10, 4)
    signed_transfer = sign_transaction(wallet, transfer_transaction)
    print(signed_transfer)
```

#### Get balance
The balance of a given token in a wallet, across wallets or all tokens in a wallet can be obtained with get balance function.
```python
    node.get_balance(balance_type, wallet_address, token_code)
```
Example
```python
    node.get_balance('TOKEN_IN_WALLET', '0xc29193dbab0fe018d878e258c93064f01210ec1a', 9)
```

#### Validate transaction
A singed transaction need to be validated to be added to the chain.
```python
    validate_result = node.validate_transaction(signed_transfer)
    print(validate_result)
```

#### Run updater
Run the miner to create a new block out of the transactions. If no valid transactions are found then an empty block will be created. This operation is not meant to be called and supposed to be run automatically by a chosen node at different intervals of time.
```python
    response = node.run_updater()
    print(response)
```

