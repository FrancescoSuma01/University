def main():
    S = set()

    with open("mails.txt") as f:
        for m in f:
            S.add(m.strip().lower())


    with open("mails_corretto.txt", 'w') as f:
        for m in S:
            f.write(m+'\n')

if __name__ == "__main__":
    main()