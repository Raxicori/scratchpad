import sys, pickle

def main(argv):
    new_leaderboard=[['Name1', '100'], ['Name2', '95'], ['Name3', '90']]
    for i in range(0,len(new_leaderboard)):
        print new_leaderboard[i]
    new_board = open('leaderboard.pkl', 'wb')
    pickle.dump(new_leaderboard, new_board)
    
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))