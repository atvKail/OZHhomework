def main():
    n = int(input().strip())

    sch_counts = {}

    for _ in range(n):
        _, _, sch_number = input().strip().split()
        if sch_number in sch_counts:
            sch_counts[sch_number] += 1
        else:
            sch_counts[sch_number] = 1

    max_count = max(sch_counts.values())

    sch_w_max_participants = [sch for sch, count in sch_counts.items() if count == max_count]
    
    for school in sorted(sch_w_max_participants):
        print(school)

if __name__ == "__main__":
    main()
