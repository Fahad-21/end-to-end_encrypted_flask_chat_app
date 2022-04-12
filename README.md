# end-to-end_encrypted_flask_chat_app
end to end encrypted chat app with python
The chat is encrypted using AES encryption which is advance encryption standard. The most popular and widely adopted symmetric encryption algorithm likely to be encountered now a days is the advanced encryption standard (AES). It is found at least six time faster than triple DES.
The user will be authenticated first via an OTP, which is sent to his email to verify the user. After the user is verified, they can have real time chat where those messages will be encrypted using the key and any users having the same kay can access (decrypt) those encrypted messages.
Socket.io is used to send and receive these messages and sent to the user having the key to decrypt them. 
