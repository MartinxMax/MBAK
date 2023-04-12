#!/usr/bin/python3
# @Мартин.
import sys, argparse, textwrap, requests, random
import concurrent.futures
import time

from loguru import logger


Version = "@Мартин. MBAK Tool V1.0.0"
Title = '''
************************************************************************************
<免责声明>:本工具仅供学习实验使用,请勿用于非法用途,否则自行承担相应的法律责任
<Disclaimer>:This tool is onl y for learning and experiment. Do not use it for illegal purposes, or you will bear corresponding legal responsibilities
************************************************************************************'''
Logo = f'''
                                                                                
        ___________        ______  ______      _____         ______   _______   
       /           \       \     \|\     \   /      |_      |\     \  \      \  
      /    _   _    \       |     |\|     | /         \      \\     \  |     /| 
     /    //   \\    \      |     |/____ / |     /\    \      \|     |/     //  
    /    //     \\    \     |     |\     \ |    |  |    \      |     |_____//   
   /     \\_____//     \    |     | |     ||     \/      \     |     |\     \   
  /       \ ___ /       \   |     | |     ||\      /\     \   /     /|\|     |  
 /________/|   |\________\ /_____/|/_____/|| \_____\ \_____\ /_____/ |/_____/|  
|        | |   | |        ||    |||     | || |     | |     ||     | / |    | |  
|________|/     \|________||____|/|_____|/  \|_____|\|_____||_____|/  |____|/   
                                                                                
              Github==>https://github.com/MartinxMax    
                {Version}  '''


def Init_Loger():
    logger.remove()
    logger.add(
        sink=sys.stdout,
        format="<green>[{time:HH:mm:ss}]</green><level>[{level}]</level> -> <level>{message}</level>",
        level="INFO"
    )


class Main_Class():
    def __init__(self, args):
        self.URL = args.URL
        self.User_Agents = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 Mobile/14F89 Safari/602.1'
        ]



    def Get_List(self):
        with open("Webdir.txt", 'r', encoding='utf-8') as f:
            self.data = f.readlines()


    def Run(self):
        if 'http' in self.URL and self.URL:
            self.Get_List()
            logger.info("Successfully loaded...")
            N = 10
            sublists = [self.data[i:i + len(self.data) // N] for i in range(0, len(self.data), len(self.data) // N)]
            with concurrent.futures.ThreadPoolExecutor(max_workers=N) as executor:
                [executor.submit(self.Process_Data, d) for sublist in sublists for d in sublist]
            logger.warning(f"{len(self.data)} tasks completed in total")
        else:
            logger.error("Please fill in the URL parameters!")


    def Process_Data(self,data):
        time.sleep(random.randint(0, 1))
        try:
            response = requests.get(self.URL + data.strip(),headers={'User-Agent':random.choice(self.User_Agents)},timeout=5)
        except Exception as e:
            logger.error("Network Timeout!")
            return False
        else:
            if response.status_code == 200:
                logger.warning(f"[{response.status_code}] [{len(response.text)}] => {self.URL + data.strip()}")


def main():
    print(Logo, "\n", Title)
    Init_Loger()
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
        Example:
            author-Github==>https://github.com/MartinxMax
        Basic usage:
            python3 {MBAK} -url "http://xxx.com/" 
            '''.format(MBAK=sys.argv[0]
                       )))
    parser.add_argument('-url', '--URL', default='', help='Target_URL')
    args = parser.parse_args()
    Main_Class(args).Run()


if __name__ == '__main__':
    main()



    


