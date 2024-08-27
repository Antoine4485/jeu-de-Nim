import random


class Nim:

    def __init__(self, nb_batonnets_restants=20, nb_batonnets_mini=1, nb_batonnets_maxi=3, mode_ia=False):
        while True:
            nim = NimGame(nb_batonnets_restants, nb_batonnets_mini, nb_batonnets_maxi, mode_ia)
            if nim.is_last_game:
                return


class NimGame:

    def __init__(self, nb_batonnets_restants, nb_batonnets_mini, nb_batonnets_maxi, mode_ia):
        self.__nb_batonnets_restants = nb_batonnets_restants
        self.__nb_batonnets_mini = nb_batonnets_mini
        self.__nb_batonnets_maxi = nb_batonnets_maxi
        self.__mode_ia = mode_ia
        self.__is_last_game = False
        self.__play()

    @property
    def is_last_game(self):
        return self.__is_last_game

    @is_last_game.setter
    def is_last_game(self, is_last_game):
        self.__is_last_game = is_last_game

    def __play(self):
        self.__show_grid()

        while True:
            for joueur_actuel in ["ordi", "vous"]:
                if joueur_actuel == "ordi":
                    nb_batonnets_pris = self.__get_nb_batonnets_pris_par_ordi()
                    print(f"L'ordinateur en prend {nb_batonnets_pris}")
                else:
                    nb_batonnets_pris = self.__get_nb_batonnets_pris_par_joueur()

                self.__nb_batonnets_restants -= nb_batonnets_pris
                if self.__nb_batonnets_restants <= 0:
                    print("Perdu !" if joueur_actuel == "ordi" else "Gagné !")
                    while True:
                        rep = input("Voulez-vous rejouer (o/n) ? ").lower()
                        if rep in ("o", "n"):
                            self.is_last_game = True if rep == "n" else False
                            break
                    return

                self.__show_grid()

    def __get_nb_batonnets_pris_par_ordi(self):
        if self.__mode_ia:
            if self.__nb_batonnets_restants <= self.__nb_batonnets_maxi:
                return self.__nb_batonnets_restants
            if self.__nb_batonnets_restants == self.__nb_batonnets_maxi + 2:
                return 1

        return random.randint(self.__nb_batonnets_mini, self.__get_nb_max_batonnets_a_jouer())

    def __get_nb_batonnets_pris_par_joueur(self):
        nb_batonnets_pris = ""
        while not (nb_batonnets_pris.isdigit() and
                   int(nb_batonnets_pris) in range(self.__nb_batonnets_mini,
                                                   self.__get_nb_max_batonnets_a_jouer() + 1)):
            nb_batonnets_pris = input(f"Combien en prenez-vous (entre {self.__nb_batonnets_mini} et"
                                      f" {self.__get_nb_max_batonnets_a_jouer()}) ? ")

        return int(nb_batonnets_pris)

    def __get_nb_max_batonnets_a_jouer(self):
        return min(self.__nb_batonnets_maxi, self.__nb_batonnets_restants)

    def __show_grid(self):
        print(("*  " * self.__nb_batonnets_restants + "\n") * 3)


if __name__ == '__main__':
    Nim(mode_ia=True)