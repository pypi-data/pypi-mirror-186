import os
import ecdsa
import codecs
import base64
from Crypto.Hash import keccak


def get_address_from_public_key(public_key_hex):
    public_key_bytes = bytes.fromhex(public_key_hex)

    wallet_hash = keccak.new(digest_bits=256)
    wallet_hash.update(public_key_bytes)
    keccak_digest = wallet_hash.hexdigest()

    address = '0x' + keccak_digest[-40:]
    return address


def get_wallet_from_private(private_key_hex):
    private_key_bytes = bytes.fromhex(private_key_hex)
    key_data = {'public': None, 'private': None, 'address': None}
    key = ecdsa.SigningKey.from_string(
        private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()

    private_key_hex = private_key_bytes.hex()
    public_key_hex = key_bytes.hex()
    key_data['address'] = get_address_from_public_key(public_key_hex)
    key_data['private'] = private_key_hex
    key_data['public'] = public_key_hex
    return key_data


def generate_wallet_address():
    private_key_bytes = os.urandom(32)
    key_data = {'public': None, 'private': None, 'address': None}
    key = ecdsa.SigningKey.from_string(
        private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()

    private_key_hex = private_key_bytes.hex()
    public_key_hex = key_bytes.hex()
    key_data['address'] = get_address_from_public_key(public_key_hex)
    key_data['private'] = private_key_hex
    key_data['public'] = public_key_hex
    return key_data


def generate_contract_address():
    private_key_bytes = os.urandom(32)
    key = ecdsa.SigningKey.from_string(
        private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()
    public_key = codecs.encode(key_bytes, 'hex')
    public_key_bytes = codecs.decode(public_key, 'hex')
    hash = keccak.new(digest_bits=256)
    hash.update(public_key_bytes)
    keccak_digest = hash.hexdigest()
    # this overwrites the None value in the init call, whenever on-chain contract is setup
    address = 'ct' + keccak_digest[-40:]
    return address

