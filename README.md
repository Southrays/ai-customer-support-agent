# AI Customer Support Agent

An AI-powered customer support agent that monitors incoming Gmail messages, classifies customer enquiries, and assists with handling support requests.

## Features
- Gmail integration for retrieving incoming emails.
- AI-powered email classification and response generation.
- Ticket creation and management.
- Persistent storage using PostgreSQL.
- Automated email polling and processing.
- Configurable AI models.

## Tech Stack
- **Python**
- **Pydantic Settings**
- **Psycopg 3**
- **PostgreSQL (Supabase)**
- **Anthropic Claude**
- **Gmail API**

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-customer-support-agent
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Configure your environment variables in a `.env` file.

4. Run the application:
   ```bash
   uv run python -m app.poller
   ```

## Configuration

The application requires environment variables for:
- Google OAuth credentials
- Database connection URL
- AI model configuration
- Dashboard credentials

See `.env.example` for the required variables.

## License

MIT