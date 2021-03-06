##Script de ejecución de la función transacción: Con la llave privada del medidor se firman las transacciones para subir a la blockchain los datos de hash de códigos del medidor, energía y estampa de tiempo 

import json
#Import web3 lib and connect with infura node
from web3 import Web3
def transaction(nit, calf, comen):
 nit = str(nit)
 calf = int(calf)
 comen = str(comen)
 print("app.py Corriendo.....")
 infura_url = "https://rinkeby.infura.io/v3/162c6026989446e08fb54b3fe3888f12"
 web3 = Web3(Web3.HTTPProvider(infura_url))
 print ("Conectado con Infura: " + str(web3.isConnected()))
 #Public key
 account = web3.toChecksumAddress("0x12e5572ee6fc57D32f4500a792712ee5f8Cdb541")
 #Private Key
 private_key = "54e254dfec678b4c1ed8373ece62ecea47008b6ffb4ac036066e885c735b240f"
 abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"ID2inscrito","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"IDa","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"IDp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"IDu","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"NombreProveedor2ID","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"admins","outputs":[{"internalType":"string","name":"nombre","type":"string"},{"internalType":"string","name":"cc","type":"string"},{"internalType":"string","name":"email","type":"string"},{"internalType":"address","name":"admin_address","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_nombre","type":"string"},{"internalType":"string","name":"_nit","type":"string"},{"internalType":"string","name":"_ciudad","type":"string"}],"name":"anotar_proveedor","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_nombre","type":"string"}],"name":"consultar_estado_proveedor","outputs":[{"internalType":"bool","name":"_inscrito","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_nombre","type":"string"},{"internalType":"string","name":"_cc","type":"string"},{"internalType":"string","name":"_email","type":"string"},{"internalType":"address","name":"_admin_address","type":"address"}],"name":"new_admin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_nombre","type":"string"},{"internalType":"string","name":"_cc","type":"string"},{"internalType":"string","name":"_email","type":"string"},{"internalType":"address","name":"_user_address","type":"address"}],"name":"new_user","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"proveedores","outputs":[{"internalType":"string","name":"nombre","type":"string"},{"internalType":"string","name":"nit","type":"string"},{"internalType":"string","name":"ciudad","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_nit","type":"string"}],"name":"puntaje_proveedor","outputs":[{"internalType":"uint256","name":"_puntaje_prom","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_nit","type":"string"},{"internalType":"uint256","name":"_calificacion","type":"uint256"},{"internalType":"string","name":"_comentarios","type":"string"}],"name":"review_prov","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"usuarios","outputs":[{"internalType":"string","name":"nombre","type":"string"},{"internalType":"string","name":"cc","type":"string"},{"internalType":"string","name":"email","type":"string"},{"internalType":"address","name":"user_address","type":"address"}],"stateMutability":"view","type":"function"}]')
 contractAddress = web3.toChecksumAddress("0x3ecD2b5D67694240945c66aeb356dDcFbf0Df654")
 #print (web3.isAddress('0x341401DCe923952ec27D9D890c4d7956947EC619'))
 contract = web3.eth.contract(address=contractAddress, abi=abi)
 #  print ("NIT: " + nit)
 #  print ("Calificación: " + calf)
 #  print ("Comentario: " + comen)
 #contract.functions.newHash(var1).transact()
 nonce = web3.eth.getTransactionCount(account)
 data_tx = contract.functions.review_prov(nit, calf, comen).buildTransaction({
    #'chainId': 0x1,
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'nonce': nonce,
    })

 print(data_tx)
 # Sign transaction
 signed_tx = web3.eth.account.signTransaction(data_tx, private_key=private_key)
 signed_tx.rawTransaction
 #Broadcast transaction
 tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
 #web3.eth.sendRawTransaction(signed_tx.rawTransaction)
 print ("Hash de la transacción: " + str(web3.toHex(tx_hash)))
