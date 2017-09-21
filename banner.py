import os, sys
"""Takes a string and outputs a banner of that string.
"""
def create_banner_text(name):
    """Create the text for the middle of the banner."""
    bannerText = "* "+str(name)+" *"
    return bannerText

def create_banner_edge(bannerText):
    """Create the edge that will be used along the top and the bottom."""
    bannerEdge=""
    for i in range(len(bannerText)):
        bannerEdge+="*"
    return bannerEdge

def main(argv):
    bannerText = create_banner_text(str(argv[0]))
    bannerEdge = create_banner_edge(bannerText)
    """Print everything in the correct order."""
    print bannerEdge
    print bannerText
    print bannerEdge
    
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))