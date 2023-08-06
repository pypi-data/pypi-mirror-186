import json
import hashlib
import time
from typing import List, Optional

from .wallet import get_address_from_public_key


def get_transaction_code(transaction):
    trstr = json.dumps(transaction).encode()
    hs = hashlib.blake2b(digest_size=20)
    hs.update(trstr)
    return hs.hexdigest()


def add_wallet_transaction(
    public_key: str,
    custodian_address: str,
    owner_type: int = 1,
    kyc_docs: List[dict] = [],
    jurisdiction: str = '',
    specific_data: dict = {},
) -> dict:
    """
        Create a transaction for adding a wallet to chain
    """
    address = get_address_from_public_key(public_key)

    wallet_data = {
        'wallet_public': public_key,
        'custodian_wallet': custodian_address,
        'ownertype': owner_type,
        'kyc_docs': kyc_docs,
        'jurisd': jurisdiction,
        'specific_data': specific_data,
        'wallet_address': address,
    }

    transaction = {
        'timestamp': int(time.time() * 1000),
        'type': 1,
        'currency': "NWRL",
        'fee': 0.0,
        'descr': "",
        'specific_data': wallet_data,
    }

    transaction['trans_code'] = get_transaction_code(transaction)

    full_transaction = {'transaction': transaction, 'signatures': []}
    return full_transaction


def add_token_transaction(
    token_code: str,
    token_type: int,
    custodian_address: str,
    first_owner: str,
    amount: int,
    token_name: Optional[str] = None,
    token_attributes: Optional[dict] = {},
    legal_doc_hash: str = '',
    token_decimal: int = 0,
    disallowed_regions: List[str] = []
) -> dict:
    if token_name is None:
        token_name = token_code

    token_data = {
        "tokencode": token_code,
        "tokentype": token_type,
        "custodian": custodian_address,
        "first_owner": first_owner,
        "amount_created": amount,

        "tokenname": token_name,
        "tokenattributes": token_attributes,
        "legaldochash": legal_doc_hash,
        "tokendecimal": token_decimal,
        "disallowed": disallowed_regions,
        "sc_flag": False
    }

    transaction = {
        'timestamp': int(time.time() * 1000),
        'type': 2,
        'currency': "NWRL",
        'fee': 0.0,
        'descr': "",
        'specific_data': token_data,
    }

    transaction['trans_code'] = get_transaction_code(transaction)

    full_transaction = {'transaction': transaction, 'signatures': []}
    return full_transaction


def add_transfer_transaction(
    transfer_type: int,
    asset1_code: str,
    asset2_code: str,
    wallet1_address: str,
    wallet2_address: str,
    asset1_qty: float,
    asset2_qty: float,
    description: str = '',
    additional_data: dict = {}
) -> dict:
    transaction_data = {
        "transfer_type": transfer_type,
        "asset1_code": str(asset1_code),
        "asset2_code": str(asset2_code),
        "wallet1": wallet1_address,
        "wallet2": wallet2_address,
        "asset1_number": int(asset1_qty),
        "asset2_number": int(asset2_qty),
        "additional_data": additional_data
    }

    transaction = {
        'timestamp': int(time.time() * 1000),
        'type': transfer_type,
        'currency': "NWRL",
        'fee': 0.0,
        'descr': description,
        'specific_data': transaction_data,
    }

    transaction['trans_code'] = get_transaction_code(transaction)

    full_transaction = {'transaction': transaction, 'signatures': []}
    return full_transaction


def add_smart_contract_transaction(
    sc_address: str,
    sc_name: str,
    version: str,
    creator: str,
    signatories: dict,
    contractspecs: dict,
    actmode: str = "hybrid",
    legalparams: dict = {},
) -> dict:
    smart_contract_data = {
        "creator": creator,
        "name": sc_name,
        "version": version,
        "actmode": actmode,
        "signatories": signatories,
        "contractspecs": contractspecs,
        "legalparams": legalparams,
        "ts_init": None,
        "status": 0,
        "next_act_ts": None,
        "parent": None,
        "oracleids": None,
        "selfdestruct": 1,
    }

    transaction_data = {
        "address": sc_address,
        "function": "setup",
        "signers": [creator],
        "params": smart_contract_data
    }

    transaction = {
        'timestamp': int(time.time() * 1000),
        'type': 3,
        'currency': "NWRL",
        'fee': 0.0,
        'descr': '',
        'specific_data': transaction_data,
    }

    transaction['trans_code'] = get_transaction_code(transaction)

    full_transaction = {'transaction': transaction, 'signatures': []}
    return full_transaction


def call_smart_contract_transaction(
    sc_address: str,
    function_called: str,
    signers: List[str],
    params: dict,
) -> dict:
    transaction_data = {
        "address": sc_address,
        "function" : function_called,
        "signers" : signers,
        "params" : params
    }

    transaction = {
        'timestamp': int(time.time() * 1000),
        'type': 3,
        'currency': "NWRL",
        'fee': 0.0,
        'descr': '',
        'specific_data': transaction_data,
    }

    transaction['trans_code'] = get_transaction_code(transaction)

    full_transaction = {'transaction': transaction, 'signatures': []}
    return full_transaction
