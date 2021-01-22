from superhero_api import SuperHeroAPI, API_KEY


class SuperHeroApp():
    def __init__(self):
        self._s = SuperHeroAPI(API=API_KEY)
        self._status = True
        self._text = """ Добро пожаловать в Супергеройское приложение.
        Доступные команды:
        help - список всех команд
        compare name name - сравнить по силе двух супергероев
        exit - выход из приложения"""

    def _set_status(self):
        self._status = False

    def run(self):
        print(self._text)
        while self._status:
            _input = input('Введите команду или help для помощи: ')
            command = self._parse_command(_input)
            self._command_dispatcher(command)

    def _parse_command(self, _input):
        return _input.strip().lower().split()

    def _command_dispatcher(self, command):
        if len(command) <= 1:
            if not command or command[0] == 'exit':
                self._set_status()
            elif command[0] == 'help':
                print(self._text)
        else:
            action, *arguments = command
            if action == 'compare':
                self._compare_heroes(arguments)

    def _compare_heroes(self, heroes):
        hero_one = self._s.get_hero_stats(heroes[0])
        hero_two = self._s.get_hero_stats(heroes[1])
        power_one, hp_one = int(hero_one['power']), int(hero_one['durability'])
        power_two, hp_two = int(hero_two['power']), int(hero_two['durability'])
        if hp_two - power_one > hp_one - power_two:
            print(f'{heroes[1].title()} победил! Осталось здоровья: {hp_two - power_one}')
        else:
            print(f'{heroes[0].title()} победил! Осталось здоровья: {hp_one - power_two}')



if __name__ == '__main__':
    app = SuperHeroApp()
    app.run()
