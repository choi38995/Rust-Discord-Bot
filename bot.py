# api 호출하기 위해 import requests; 추가
#import requests;
# 환경 변수를 읽게 하기 위해 import os; 추가
# 파이썬 기본 기능인 os 모듈을 가져오기 위해 import os; 추가
import os
from re import search;
# 디스코드 봇을 만들기 위해 import discord; 추가
import discord;
# 디스코드드 봇 명령어를 만들기 위해 추가
# commands 모듈을 discord.ext.commands에서 가져오기
# 필요한 기능만 가져오기 위해 form을 사용하여 import 하기
from discord.ext import commands
#.env 파일에서 환경 변수를 로드하기 위해 import load_dotenv; 추가
from dotenv import load_dotenv
import requests;

# .env 파일에서 환경 변수를 로드하기 위해 load_dotenv() 함수 호출
load_dotenv();

# DISCORD_TOKEN 환경 변수를 읽어서 TOKEN 변수에 저장
TOKEN = os.getenv('DISCORD_TOKEN');

# 디스코드 클라이언트 객체 생성
whatInfo = discord.Intents.default();
# 메시지 내용을 읽을 수 있도록 message_content 권한 활성화
whatInfo.message_content = True;

# 명령어 프리픽스 설정과 권한 설정을 사용하여 봇 객체 생성
bot = commands.Bot(command_prefix='/', intents=whatInfo);

# def란? 사용자 정의 함수를 생성할 때 사용하는 키워드
def serarch_keyword(keyword: str):
    url = "https://api.battlemetrics.com/servers";
    # 15초 안에 응답이 안올 경우 실패 처리
    # 좀 늦는 경우가 있어 20초 정도로 잡음
    response = requests.get(url, timeout=20)
    response.raise_for_status()  # HTTP 오류가 발생하면 예외를 발생시킴
    # 데이터 추출
    data = response.json()
    servers = data.get('data', []); # data가 없을경우 빈값 배열

    # 검색어 기반이기 때문에 포함 된 것만 필터링해 결과값 반환
    results = []

    # for문은 반복 가능한 객체의 요소를 처음부터 끝까지 하나씩 꺼내 코드 불록을 생성하는 구조
    # for 변수 in 반복 가능한 객체:
    for server in servers:
        # 딕셔너리(server)에서 'attributes' 키에 해당하는 값을 가져오고, 없으면 빈 딕셔너리를 반환
        attributes = server.get('attributes', {})
        name = attributes.get('name', '')
        # keyword가 name에 포함되어 있는지 확인 (대소문자 구분 없이)
        if keyword.lower() in name.lower():
            results.append(server)
    return results;

# 서버 ID로 검색하는 함수
def search_server_details(id: str):
    # 서버 상세 정보를 반환하는 함수
    url = f"https://api.battlemetrics.com/servers/{id}"
    response = requests.get(url, timeout=20)
    response.raise_for_status()  # HTTP 오류가 발생하면 예외를 발생시킴
    data = response.json()
    server = data.get('data', {})  

    return server;

# 봇이 준비되었을 때 실행되는 이벤트 핸들러 정의
@bot.event
async def on_ready():
    print(f'{bot.user} 연결 완료!'); 

# 'ping' 명령어가 호출되었을 때 실행되는 명령어 핸들러 정의
# 명령어 이름은 'server'이고, 도움말 메시지는 '전체 서버 리스트'로 설정
# /search keyword 같은 명령어를 처리하기 위해 작업중
# *이 들어간 이유는 검색어에 공백이 들어갈 수 있기 때문임
# ctx는 명령어가 호출된 컨텍스트(요청 정보)를 나타내며, keyword는 명령어에 전달된 검색어를 나타냄
@bot.command(name="검색어", help='서버이름 검색어')
async def search_server(ctx, *, keyword: str):
    try:
        servers = serarch_keyword(keyword)
        if not servers:
            await ctx.send('검색 결과가 없습니다.');
            return;
        buffer = [f"'{keyword}' 검색 결과"]

        # 10개까지만 보여주는 설정
        for indx, server in enumerate(servers[:10], start=1):
            server_id = server.get('id', '정보없음')
            attributes = server.get('attributes', {})

            name = attributes.get('name', '정보없음')
            player_count = attributes.get('players', '정보없음')
            max_players = attributes.get('maxPlayers', '정보없음')
            status = attributes.get('status', '정보없음')   
            country = attributes.get('country', '정보없음')

            buffer.append(f"{indx}. {name} (ID: {server_id}, 플레이어 수: {player_count}/{max_players}, 상태: {status}, 국가: {country})")
        
        buffer.append(f"   상세 정보: /server_details {server_id}")
        message = "\n".join(buffer)
        await ctx.send(message);

    except Exception as e:
        await ctx.send(f"오류가 발생했습니다: {str(e)}");


@bot.command(name="id", help='서버 ID로 상세 정보 검색')
async def server_details(ctx, server_id: str):
    try:
        server = search_server_details(server_id)
        if not server:
            await ctx.send('서버를 찾을 수 없습니다.')
            return

        attributes = server.get('attributes', {})
        name = attributes.get('name', '정보없음')
        player_count = attributes.get('players', '정보없음')
        max_players = attributes.get('maxPlayers', '정보없음')
        status = attributes.get('status', '정보없음')
        country = attributes.get('country', '정보없음')
        address = attributes.get('ip', '정보없음')
        port = attributes.get('port', '정보없음')
        map_name = attributes.get('map', '정보없음')
        map_size = attributes.get('mapSize', '정보없음')

        message = (f"서버 이름: {name}\n"
                   f"플레이어 수: {player_count}/{max_players}\n"
                   f"상태: {status}\n" 
                   f"국가: {country}\n" 
                   f"주소: {address}:{port}\n"
                   f"맵 이름: {map_name}\n"
                   f"맵 크기: {map_size}")
        await ctx.send(message)

    except Exception as e:
        await ctx.send(f"오류가 발생했습니다: {str(e)}")


# 봇 실행
bot.run(TOKEN);