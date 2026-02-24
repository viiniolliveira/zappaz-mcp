
# Zappaz MCP Server

O Zappaz MCP Server conecta ferramentas MCP a Zappaz API de WhatsApp. Ele expoe
tools para envio e gerenciamento de mensagens (texto, imagem, video, audio,
documento, contato, localizacao) usando um sessionId e um token de sessao.

### Casos de uso

- Envio de mensagens via WhatsApp a partir de agentes MCP.
- Automacao de atendimentos com multimidia (imagem, video, audio, documento).
- Compartilhamento de contatos e localizacoes.
- Remocao de mensagens pelo id.

---

## Servidor Zappaz MCP (Remoto)

O servidor e remoto e esta disponivel em `https://mcp.zappaz.io`.

---

## Autenticacao

Todas as chamadas exigem:

- `sessionId` no query string (`?sessionId=...`)
- `Authorization` no header

Sem esses valores o servidor retorna erro.

---

## Configuracao no OpenCode

Adicione o servidor no seu `mcp.json` do OpenCode:

```json
{
  "servers": {
    "zappaz-mcp": {
      "type": "remote",
      "enabled": true,
      "url": "https://mcp.zappaz.io/mcp?sessionId=YOUR_SESSION",
      "headers": {
        "Authorization": "YOUR_SESSION_TOKEN"
      }
    }
  }
}
```

## Configuracao no Cursor

Crie o arquivo `.cursor/mcp.json` com a entrada abaixo:

```json
{
  "mcpServers": {
    "zappaz-mcp": {
      "type": "remote",
      "enabled": true,
      "url": "https://mcp.zappaz.io/mcp?sessionId=YOUR_SESSION",
      "headers": {
        "Authorization": "YOUR_SESSION_TOKEN"
      }
    }
  }
}
```

## Configuracao no Antigravity

No Agent Panel, clique nos tres pontos no canto superior direito e selecione
MCP Servers. Clique em Manage MCP Servers. Selecione "View raw config" e adicione:

```json
{
  "mcpServers": {
    "zappaz-mcp": {
      "type": "remote",
      "enabled": true,
      "serverUrl": "https://mcp.zappaz.io/mcp?sessionId=YOUR_SESSION",
      "headers": {
        "Authorization": "YOUR_SESSION_TOKEN"
      }
    }
  }
}
```

## Configuracao no VS Code

Abra a Command Palette (Cmd+Shift+P) e digite "MCP: Add Server". Selecione
"Add MCP Server". Escolha HTTP para adicionar um MCP remoto. Informe a URL
`https://mcp.zappaz.io/mcp?sessionId=YOUR_SESSION` e o nome `zappaz-mcp`.

Depois, edite o `mcp.json` para adicionar o header de autorizacao:

```json
{
  "servers": {
    "zappaz-mcp": {
      "type": "remote",
      "enabled": true,
      "url": "https://mcp.zappaz.io/mcp?sessionId=YOUR_SESSION",
      "headers": {
        "Authorization": "YOUR_SESSION_TOKEN"
      }
    }
  }
}
```

## Configuracao no Claude Desktop

Adicione o servidor no seu arquivo de configuracao MCP:

```json
{
  "servers": {
    "zappaz-mcp": {
      "type": "remote",
      "enabled": true,
      "url": "https://mcp.zappaz.io/mcp?sessionId=YOUR_SESSION",
      "headers": {
        "Authorization": "YOUR_SESSION_TOKEN"
      }
    }
  }
}
```

## Configuracao no Claude Code

Adicione o servidor no seu arquivo de configuracao MCP:

```json
{
  "servers": {
    "zappaz-mcp": {
      "type": "remote",
      "enabled": true,
      "url": "https://mcp.zappaz.io/mcp?sessionId=YOUR_SESSION",
      "headers": {
        "Authorization": "YOUR_SESSION_TOKEN"
      }
    }
  }
}
```

## Configuracao no Windsurf

Adicione o servidor no seu arquivo de configuracao MCP:

```json
{
  "servers": {
    "zappaz-mcp": {
      "type": "remote",
      "enabled": true,
      "url": "https://mcp.zappaz.io/mcp?sessionId=YOUR_SESSION",
      "headers": {
        "Authorization": "YOUR_SESSION_TOKEN"
      }
    }
  }
}
```

---

## Tools disponiveis

| Tool | Descricao |
| --- | --- |
| `send_text_message` | Envia mensagem de texto. |
| `send_image_message` | Envia mensagem de imagem. |
| `send_video_message` | Envia mensagem de video. |
| `send_audio_message` | Envia mensagem de audio. |
| `send_document_message` | Envia mensagem de documento. |
| `send_contact_message` | Envia mensagem com contato. |
| `send_location_message` | Envia mensagem com localizacao. |
| `delete_message` | Deleta uma mensagem por id. |

---

---

## Observacoes

- O token e o sessionId sao obrigatorios para todas as chamadas.
