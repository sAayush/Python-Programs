class City:
    def destCity(self, paths: list[list[str]]) -> str:
        if len(paths) == 1:
            return paths[0][1]
        else:
            for i in range(len(paths)):
                for j in range(len(paths)):
                    if paths[i][1] == paths[j][0]:
                        break
                    if j == len(paths) - 1:
                        return paths[i][1]
            return ""


if __name__ == '__main__':
    city = City()
    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    print(city.destCity(paths))
