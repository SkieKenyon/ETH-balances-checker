from web3 import Web3

# Replace 'YOUR_INFURA_PROJECT_ID' with your Infura project ID
# You can get a free project ID by signing up on https://infura.io/
INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'

# List of Ethereum wallet addresses to check
wallet_addresses = [
    '0xWalletAddress1',
    '0xWalletAddress2',
    # Add more wallet addresses as needed
]

# Initialize a web3 provider using Infura
w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))

def get_balance(wallet_address):
    try:
        balance = w3.eth.get_balance(wallet_address)
        return w3.fromWei(balance, 'ether')
    except Exception as e:
        return f"Error getting balance for {wallet_address}: {str(e)}"

if __name__ == "__main__":
    for address in wallet_addresses:
        balance = get_balance(address)
        print(f"Balance for {address}: {balance} ETH")
