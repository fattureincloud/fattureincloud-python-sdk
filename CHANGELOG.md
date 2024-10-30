# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### 2.1.2 (2024-10-30)

### 2.1.1 (2024-10-24)

## 2.1.0 (2024-06-17)

### 2.0.20 (2024-05-27)

### 2.0.19 (2024-05-06)

### 2.0.19 (2024-05-06)

### 2.0.18 (2024-03-06)

### 2.0.17 (2023-12-07)

### 2.0.16 (2023-10-09)

### 2.0.15 (2023-07-18)

### 2.0.14 (2023-05-10)

### 2.0.13 (2023-05-04)

### 2.0.12 (2023-02-15)

#### Changed models imports

before:

```py
fattureincloud_python_sdk.model.some_model
```

now:

```py
fattureincloud_python_sdk.models.some_model
```

### Changed Configuration constructor

setting the access token before:

```py
configuration = fattureincloud_python_sdk.Configuration(
    access_token = "YOUR_ACCESS_TOKEN"
)
```

now:

```py
configuration = fattureincloud_python_sdk.Configuration()
configuration.access_token = "YOUR_ACCESS_TOKEN"
```

### 2.0.11 (2022-12-14)

### 2.0.10 (2022-11-21)

### 2.0.9 (2022-09-22)

### 2.0.8 (2022-07-19)

### 2.0.7 (2022-06-20)

### 2.0.6 (2022-05-13)

### Bug Fixes

- released has_intent_declaration param ([#41](https://github.com/fattureincloud/fattureincloud-python-sdk/issues/41)) ([286c342](https://github.com/fattureincloud/fattureincloud-python-sdk/commit/286c342abcfff84d48c5bf80c2cc7bed383ddc45))

### 2.0.5 (2022-05-12)

### 2.0.4 (2022-04-21)

### 2.0.3 (2022-03-17)

### Bug Fixes

- added filter parameter and detailed countries method ([#15](https://github.com/fattureincloud/fattureincloud-python-sdk/issues/15)) ([56a4415](https://github.com/fattureincloud/fattureincloud-python-sdk/commit/56a4415d185b129d657ae0a16f41e5fb16da4c9b))

### 2.0.2 (2022-02-28)

### Bug Fixes

- models are now nullable ([1b96d33](https://github.com/fattureincloud/fattureincloud-python-sdk/commit/1b96d334b62315e29d5cf93cf4b913ca17bba7c8))

### 2.0.1 (2022-02-14)
