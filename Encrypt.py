import pandas as pd

class Encryption:

    def __init__(self) -> None:
        self.encryption_key = pd.read_csv("./decodekeynew.csv", sep=",", names=["Character", "Byte"])
        self.df = pd.DataFrame(self.encryption_key)
        self.df['Character'] = self.df['Character'].astype(str)
        self.df['Byte'] = self.df['Byte'].astype(str)

    def __Encode(self, message):
        coded_msg = ""
        for i in range(len(message)):
            j = message[i]
            try:
                coded_char = self.encryption_key.loc[self.encryption_key['Character'] == j, 'Byte'].iloc[0]
            except:
                return f"Unrecognized Character {j}"
            coded_msg += coded_char
        return coded_msg

    def __Decode(self, encrypted):
        decoded_msg = []
        for i in range(0, len(encrypted), 2):
            j = encrypted[i:i+2]
            index_nb = self.df[self.df.eq(j).any(1)]
            df2 = index_nb['Character'].tolist()
            s = [str(x) for x in df2]
            decoded_msg = decoded_msg + s
        message = "".join(decoded_msg)
        return message

    def Encrypt(self, message):
        message = [char for char in message]
        return(self.__Encode(message))
    
    def Decrypt(self, encrypted):
        return self.__Decode(encrypted)

if __name__=="__main__":
    EN = Encryption()
    EN.Encrypt(input())