def sign():
    from Crypto.Hash import SHA256
    from Crypto.PublicKey import RSA
    key = RSA.generate(2048)
    public = key.publickey().exportKey('PEM').decode('ascii')
    private = key.exportKey('PEM').decode('ascii')

    text = 'abcdefgh'.encode('utf-8')
    hash = SHA256.new(text).digest()
    signature = key.sign(hash, '')
    print('signature=', signature)

sign()