import base64
import ecdsa
import json


def sign_transaction(wallet_data, transaction_data):
    address = wallet_data['address']
    private_key_bytes = bytes.fromhex(wallet_data['private'])
    if not private_key_bytes:
        print("No private key found for the address")
        return False

    msg = json.dumps(transaction_data['transaction']).encode()
    sk = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    msgsignbytes = sk.sign(msg)
    msgsign = msgsignbytes.hex()
    signatures = transaction_data['signatures'] if 'signatures' in transaction_data else [
    ]
    signatures.append({'wallet_address': address, 'msgsign': msgsign})

    return transaction_data


def addresschecker(transaction, address):
    #	trans=trandata['transaction']
    #	signatures = trandata['signatures']
    validadds = getvalidadds(transaction)
    print(validadds)
    for add in validadds:
        if add == address:
            print("The address ", address,
                  " is authorised to sign this transaction.")
            return True
        # did not find the address in the validadds
    print("The address ", address, " is not authorised to sign this transaction.")
    return False

# use the below one to get all authorized addresses that can sign a transaction


def getvalidadds(transaction):
    trans = transaction
    ttype = trans['type']
    validadds = []
    if ttype == 1:  # wallet creation, custodian needs to sign
        validadds.append(trans['specific_data']['custodian_wallet'])
    if ttype == 2:  # token creation, custodian needs to sign
        validadds.append(trans['specific_data']['custodian'])
    if ttype == 4:  # two way transfer; both senders need to sign
        validadds.append(trans['specific_data']['wallet1'])
        validadds.append(trans['specific_data']['wallet2'])
    if ttype == 5:  # one way transfer; only sender1 is needed to sign
        validadds.append(trans['specific_data']['wallet1'])
    return validadds


def verify_sign(data, signature, public_key):
    public_key_bytes = bytes.fromhex(public_key)
    sign_trans_bytes = bytes.fromhex(signature)
    vk = ecdsa.VerifyingKey.from_string(
        public_key_bytes, curve=ecdsa.SECP256k1)
    message = json.dumps(data).encode()
    try:
        return vk.verify(sign_trans_bytes, message)
    except:
        return False
