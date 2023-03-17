import sys, argparse

from movie import MovieTheater

# get arguments
def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', '--input', type=str, help='input file')
    parser.add_argument('-o', '--output', type=str, help='output file')
    args = parser.parse_args()
    inputfile = args.input
    if args.output:
        outputfile = args.output
    else:
        outputfile = inputfile.split('.')[0] + '.out'
    
    # read input file
    myMovieTheater = MovieTheater()
    with open(inputfile, 'r') as f:
        for line in f:
            inputs = line.split()
            if len(inputs) == 2:
                orderno,num_people = line.split()
                num_people = int(num_people)
                myMovieTheater.greedy_assignment(orderno, num_people)
                print(myMovieTheater)
            else:
                if inputs[0] == "-":
                    myMovieTheater.cancel_order(inputs[1:])
    # write output file
    with open(outputfile, 'w') as f:
        f.write("\n".join(myMovieTheater.output()))

if __name__ == '__main__':
    main()
