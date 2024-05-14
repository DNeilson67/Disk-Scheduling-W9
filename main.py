import sys
from fcfs import fcfs
from cscan import cscan
from scan import scan

def read_requests(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines()]
    return requests

if __name__ == "__main__":
    # It can only be run if both arguments (head, filepath) are included.
    if len(sys.argv) != 3:
        print("Usage: python main.py <start_position> <file_path>")
        exit
    
    # first argument, head must be integer
    head = int(sys.argv[1])
    # second argument, path of the file
    file_path = sys.argv[2]

    requests = read_requests(file_path)

    print("FCFS - Total Head Movement:", fcfs(requests=requests,head=head))
    print("Scan (Starting from left Direction) - Total Head Movement:", scan(requests=requests,head=head))
    print("Scan (Starting from right Direction) - Total Head Movement:", scan(requests=requests,head=head, direction="right"))
    print("CScan - Total Head Movement:", cscan(requests=requests, head=head))

    print("\nOptimized version:")
    print("FCFS - Total Head Movement:", fcfs(requests=requests,head=head,sort=True))
    print("Scan (Starting from left Direction) - Total Head Movement:", scan(requests=requests,head=head,sort=True))
    print("Scan (Starting from right Direction) - Total Head Movement:", scan(requests=requests,head=head,sort=True,direction="right"))
    print("CScan - Total Head Movement:", cscan(requests=requests, head=head,sort=True))




