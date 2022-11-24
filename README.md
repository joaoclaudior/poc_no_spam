Add arquivo .env na raiz do projeto com as variaveis:
```
AKISMET_API_KEY=<sua key>
AKISMET_BLOG_URL=<url site>
```

Primeira vez executando, executar na vpnsp:
```
docker-compose up --build
```

Demais execução em qualquer vpn
```
docker-compose up
```

Requisições em poc.json imposrtar no insomnia

