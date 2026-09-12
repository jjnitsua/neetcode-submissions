class TimeMap:

    def __init__(self):
        self.TableDic={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TableDic:
            self.TableDic[key] = {}

        self.TableDic[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.TableDic:
            return ""
        else:
            t_v=timestamp
            while t_v>=0:
                if t_v in self.TableDic[key]:
                    return self.TableDic[key][t_v]
                    break
                t_v-=1
            return ""
