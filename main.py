# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    timeris = [0]*n
    for k in range(m):
        tmin = min(timeris)
        thread = timeris.index(tmin)
        time = timeris[thread]
        output.append((thread, time))
        timeris[thread] += data[k]

    return output

def main():
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n,m = map(int,input().split())

    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int,input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread, time in result:
        print(thread, time)


if __name__ == "__main__":
    main()
