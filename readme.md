# 요약

요즘 핫한 AI 커뮤니티인 [허깅페이스]"https://huggingface.co/" 에서 쉽고 재밌는걸 해보고 있습니다.

# 설치 및 실행

약 2~3GB 정도 다운로드 받아야합니다.

```bash
pip install -r requirements.txt
python webapi.py
```


# 사용

## 문장 요약

뉴스같은 적당한 길이의 문서를 요약해줍니다.
그래픽카드가 없는 i7-11700K로 대략 20~30초 정도 소요됩니다.

```
http://127.0.0.1:5000/api/summary?text=<요약 할 텍스트>
```

## 문장 생성

문장의 나머지 부분을 자동완성 해줍니다.
0.2초 미만으로 소요됩니다.

```
http://127.0.0.1:5000/api/generate?text=마른 하늘에
```