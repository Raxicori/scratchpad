import sys, pickle, csv

"""Script to update a leaderboard
    Inputs:
        A leaderboard pickle file, this must be a list of lists
        A updates csv file, contins names and scores to add on
"""

def sort_leaderboard(leaderboard):
    """Sort the supplied leaderboard, putting the highest score first.
    """
    for i in range(1, len(leaderboard)):
        j = i
        #We want to compare just the scores, not the whole entry
        while j > 0 and leaderboard[j][1] > leaderboard[j-1][1]:
            #But we do want to write the whole entry
            leaderboard[j], leaderboard[j-1] = leaderboard[j-1], leaderboard[j]
            j -= 1
    return leaderboard

def read_current_board(leaderboard_file):
    """Unpickle the current leaderboard (or any data structure really).
    """
    old_board=open(leaderboard_file, 'rb')
    leaderboard=pickle.load(old_board)
    old_board.close()
    return leaderboard

def read_updates(updates_file):
    """Read in the updates from a csv file.
    """
    updates_CSV=open(updates_file, 'rb')
    updates = csv.reader(updates_CSV)
    return updates

def pickle_board(leaderboard):
    """Pickle a leaderboard (or any data structure really).
    """
    new_board = open('leaderboard.pkl', 'wb')
    pickle.dump(leaderboard, new_board)

def update_scores(leaderboard, updates):
    """Update the scores for each player, add any new players and record W's.
    """
    for score in updates:
        #Keep track of whether the player is new or not
        updated=False
        for player in leaderboard:
            if player[0] == score[0]:
                player[1]=int(player[1])+int(score[1])
                try:
                    #If the player won, append the W or make a new W
                    if score[2]:
                        try:
                            player[2]=player[2]+score[2]
                        except:
                            player.append(score[2])
                except:
                    pass
                updated=True
        #If its a new player they need a new entry
        if updated==False:
            #We want their score to be an int
            score[1]=int(score[1])
            leaderboard.append(score)
    return leaderboard

def main(argv):
    leaderboard=read_current_board('leaderboard.pkl')
    try:
        updates=read_updates(argv[0])
    except(IndexError):
        print "leaderboard.py: [Errno 1]: Please provide a CSV results file."
        sys.exit(0)
    
    new_leaderboard=update_scores(leaderboard, updates)
    ranked_leaderboard=sort_leaderboard(new_leaderboard)

    #Print out the new ranked leaderboard
    for i in range(0,len(ranked_leaderboard)):
        print ranked_leaderboard[i]

    #Then pickle it
    pickle_board(ranked_leaderboard)
    
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))