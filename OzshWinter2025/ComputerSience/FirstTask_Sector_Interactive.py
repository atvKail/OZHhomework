from FirstTask_Sector_Class import plot_sector_and_dividing_line


def main():
    cnt = 0
    while True:
        print(f"Необходимо ввести данные и это {cnt + 1} раз R, phi1, phi2")
        R, phi1, phi2 = map(
            int,
            input(
                "Формат ввода: 'R phi1 phi2', без скобочек и с пробелами между R и phi1, phi1 и phi2 \n> "
            ).split(),
        )
        plot_sector_and_dividing_line(R=R, phi1=phi1, phi2=phi2)
        cnt += 1


if __name__ == "__main__":
    main()
