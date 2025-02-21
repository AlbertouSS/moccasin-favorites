from src import favorites

def deploy_favorites():
    favorites_contract = favorites.deploy()
    # init_number = favorites_contract.retrieve()
    # print(f"Initial number: {init_number}")
    
    # favorites_contract.store(100)
    # final_number = favorites_contract.retrieve()
    # print(f"Final number: {final_number}")
    
    return favorites_contract
    
# this is equivalent to -> if __name__ == "main"
def moccasin_main():
    deploy_favorites()