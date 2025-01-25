<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">READMEAI_AUTO</h1></p>
<p align="center">
	<em>AI 기반 README 번역, 간편하게.
</em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. --></p>
<p align="center">다음 도구 및 기술로 구축:</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Google%20Gemini-8E75B2.svg?style=default&logo=Google-Gemini&logoColor=white" alt="Google%20Gemini">
</p>
<br>

##  목차

- [ 개요](#-개요)
- [ 기능](#-기능)
- [ 프로젝트 구조](#-프로젝트-구조)
  - [ 프로젝트 인덱스](#-프로젝트-인덱스)
- [ 시작하기](#-시작하기)
  - [ 사전 요구 사항](#-사전-요구-사항)
  - [ 설치](#-설치)
  - [ 사용법](#-사용법)
  - [ 테스트](#-테스트)
- [ 프로젝트 로드맵](#-프로젝트-로드맵)
- [ 기여](#-기여)
- [ 라이선스](#-라이선스)
- [ 감사의 말씀](#-감사의-말씀)

---

##  개요

readmeaiauto는 Google의 AI를 사용하여 README 파일을 여러 언어로 손쉽게 번역합니다. 이는 개발자를 위한 국제화를 간소화하여 전 세계적인 도달 및 접근성을 보장합니다. 주요 기능에는 자동화된 번역, 서식 유지 및 구성 가능한 언어 지원이 있습니다. 오픈 소스 프로젝트 및 다국어 팀에 이상적입니다.

---

##  기능

|      | 기능         | 요약       |
| :--- | :---:           | :---          |
| ⚙️  | **아키텍처**  | <ul><li>이 프로젝트는 `<python>` 기반 아키텍처를 활용합니다.</li><li>번역 기능을 위해 `<google-generativeai>` API를 활용합니다.</li><li>`readme_translator.py` 스크립트는 번역의 핵심 로직 역할을 합니다.</li><li>API 키와 같은 환경 변수를 관리하기 위해 `<python-dotenv>`를 사용합니다.</li></ul> |
| 🔩 | **코드 품질**  | <ul><li>코드 품질 평가는 `readme_translator.py`를 추가로 검사해야 합니다.</li><li>코딩 스타일 가이드라인(예: PEP 8) 준수 여부를 확인해야 합니다.</li><li>코드 내 주석 및 문서의 존재 여부를 평가해야 합니다.</li><li>코드 복잡성 및 유지 관리 가능성을 평가해야 합니다.</li></ul> |
| 📄 | **문서** | <ul><li>문서는 주로 `requirements.txt` 및 `readme_translator.py` 파일에서 찾을 수 있습니다.</li><li>기본 언어 감지가 실패하여 문서 명확성을 개선해야 함을 나타냅니다(`txt` 및 `py` 파일 감지됨).</li><li>`requirements.txt` 파일에는 종속성이 명확하게 나열되어 있습니다.</li><li>더 나은 이해를 위해서는 추가 문서(예: 사용법을 설명하는 README 파일)가 필요할 수 있습니다.</li></ul> |
| 🔌 | **통합**  | <ul><li>`<google-generativeai>` API(Google Gemini일 가능성이 높음)와 통합됩니다.</li><li>`requirements.txt`에 표시된 대로 종속성 관리를 위해 `<pip>`를 사용합니다.</li><li>환경 변수 관리를 위해 `<python-dotenv>`를 활용합니다.</li><li>다른 통합은 명시적으로 언급되지 않았습니다.</li></ul> |
| 🧩 | **모듈성**    | <ul><li>이 프로젝트는 전용 `readme_translator.py` 스크립트를 사용하여 모듈식 구조를 갖는 것으로 보입니다.</li><li>모듈성 수준 및 코드 재사용 가능성을 확인하기 위한 추가 분석이 필요합니다.</li><li>관심사 분리의 정도를 평가해야 합니다.</li><li>향후 확장 및 기능 추가 가능성을 고려해야 합니다.</li></ul> |
| 🧪 | **테스트**       | <ul><li>명시적인 테스트 프레임워크 또는 테스트 파일은 언급되지 않았습니다.</li><li>테스트 명령어는 자리 표시자입니다(`INSERT-TEST-COMMAND-HERE`).</li><li>테스트가 없다는 것은 잠재적인 위험을 나타냅니다.</li><li>단위 및 통합 테스트 구현이 권장됩니다.</li></ul> |
| ⚡️  | **성능**   | <ul><li>벤치마킹 없이는 성능 특성을 알 수 없습니다.</li><li>성능은 Google Generative AI API의 응답 시간과 스크립트의 효율성에 따라 달라집니다.</li><li>큰 README 파일이나 많은 번역의 경우 최적화 전략이 필요할 수 있습니다.</li><li>성능 병목 현상을 확인하기 위한 추가 분석이 필요합니다.</li></ul> |

---

##  프로젝트 구조

```sh
└── readmeai_auto/
    ├── LICENSE
    ├── README.md
    ├── README_DE.md
    ├── README_EN.md
    ├── README_ES.md
    ├── README_FR.md
    ├── README_JA.md
    ├── README_KO.md
    ├── README_RU.md
    ├── README_ZH.md
    ├── readme_translator.py
    └── requirements.txt
```


###  프로젝트 인덱스
<details open>
	<summary><b><code>READMEAI_AUTO/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='/home/jinno/git/readmeai_auto_action/readmeai_auto/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- `requirements.txt` 파일은 프로젝트의 외부 종속성을 지정합니다.<br>- 이를 통해 프로젝트에서 Google Generative AI API에 액세스하고 `python-dotenv`에서 관리하는 환경 변수를 활용할 수 있습니다.<br>- 이는 Google의 AI 서비스와의 통합을 용이하게 하여 애플리케이션이 해당 기능을 활용할 수 있도록 합니다.</td>
			</tr>
			<tr>
				<td><b><a href='/home/jinno/git/readmeai_auto_action/readmeai_auto/blob/master/readme_translator.py'>readme_translator.py</a></b></td>
				<td>- `readme_translator.py` 스크립트는 README 파일 번역을 자동화합니다.<br>- Google Gemini API를 활용하여 소스 README를 여러 언어로 번역하여 서식과 기술적 정확성을 유지합니다.<br>- 이 스크립트는 입력 파일과 대상 언어를 지정하기 위한 명령줄 옵션을 제공하며 진행 상황과 오류를 기록합니다.<br>- 지원되는 언어는 구성 가능하므로 국제화를 위한 유연성이 향상됩니다.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  시작하기

###  사전 요구 사항

readmeai_auto를 시작하기 전에 런타임 환경이 다음 요구 사항을 충족하는지 확인하세요.

- **프로그래밍 언어:** 기본 언어 감지 오류: {'txt': 1, 'py': 1}
- **패키지 관리자:** Pip


###  설치

다음 방법 중 하나를 사용하여 readmeai_auto를 설치하세요.

**소스에서 빌드:**

1. readmeai_auto 리포지토리를 복제합니다.
```sh
❯ git clone ../readmeai_auto
```

2. 프로젝트 디렉토리로 이동합니다.
```sh
❯ cd readmeai_auto
```

3. 프로젝트 종속성을 설치합니다.


**`pip` 사용** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-INSTALL-COMMAND-HERE'
```




###  사용법
다음 명령을 사용하여 readmeai_auto를 실행합니다.
**`pip` 사용** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-RUN-COMMAND-HERE'
```


###  테스트
다음 명령을 사용하여 테스트 스위트를 실행합니다.
**`pip` 사용** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-TEST-COMMAND-HERE'
```


---
##  프로젝트 로드맵

- [X] **`작업 1`**: <strike>기능 1 구현.</strike>
- [ ] **`작업 2`**: 기능 2 구현.
- [ ] **`작업 3`**: 기능 3 구현.

---

##  기여

- **💬 [토론에 참여하기](https://LOCAL/readmeai_auto_action/readmeai_auto/discussions)**: 의견을 공유하거나 피드백을 제공하거나 질문하십시오.
- **🐛 [문제 보고하기](https://LOCAL/readmeai_auto_action/readmeai_auto/issues)**: `readmeai_auto` 프로젝트에서 발견된 버그를 제출하거나 기능 요청을 기록하십시오.
- **💡 [풀 리퀘스트 제출하기](https://LOCAL/readmeai_auto_action/readmeai_auto/blob/main/CONTRIBUTING.md)**: 열린 PR을 검토하고 자신의 PR을 제출하십시오.

<details closed>
<summary>기여 가이드라인</summary>

1. **리포지토리 포크**: 먼저 프로젝트 리포지토리를 LOCAL 계정으로 포크합니다.
2. **로컬에 복제**: Git 클라이언트를 사용하여 포크된 리포지토리를 로컬 머신으로 복제합니다.
   ```sh
   git clone /home/jinno/git/readmeai_auto_action/readmeai_auto/
   ```
3. **새 브랜치 생성**: 항상 설명이 포함된 이름으로 새 브랜치에서 작업하십시오.
   ```sh
   git checkout -b new-feature-x
   ```
4. **변경 사항 적용**: 로컬에서 변경 사항을 개발하고 테스트합니다.
5. **변경 사항 커밋**: 업데이트를 설명하는 명확한 메시지로 커밋합니다.
   ```sh
   git commit -m '새 기능 x 구현.'
   ```
6. **LOCAL로 푸시**: 변경 사항을 포크된 리포지토리로 푸시합니다.
   ```sh
   git push origin new-feature-x
   ```
7. **풀 리퀘스트 제출**: 원본 프로젝트 리포지토리에 대해 PR을 생성합니다. 변경 사항과 그 동기를 명확하게 설명합니다.
8. **검토**: PR이 검토되고 승인되면 기본 브랜치에 병합됩니다. 기여해 주셔서 감사합니다!
</details>

<details closed>
<summary>기여자 그래프</summary>
<br>
<p align="left">
   <a href="https://LOCAL{/readmeai_auto_action/readmeai_auto/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=readmeai_auto_action/readmeai_auto">
   </a>
</p>
</details>

---

##  라이선스

이 프로젝트는 [SELECT-A-LICENSE](https://choosealicense.com/licenses) 라이선스에 따라 보호됩니다. 자세한 내용은 [LICENSE](https://choosealicense.com/licenses/) 파일을 참조하십시오.

---

##  감사의 말씀

- 여기에 리소스, 기여자, 영감 등을 나열하십시오.

---
