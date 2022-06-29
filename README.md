This repo is for checking banned domains  
  
HOW TO USE  
1. Create `.env` file from template `.env.temp`  
2. Run with `docker run --env-file=.env arseniiyamnii/rkn-checker`  
2. (b) Or just build image with `docker build .`, and then run 
  
Variables explanation:   
 * `ACCESS_TOKEN` gitlab access token
 * `TELEGRAM_BOT_TOKEN` telegram access token
 * `FILELINK` link to file via api: ex. `https://gitlab.com/api/v4/projects/<project id>/repository/files/<dir>%2F<filename>%2E<extemtion>/raw?ref=<branch>`
 * `REGEX_PATTERN` pattern for validate domains: ex. `^google.+\.com$` for get all `googlexxx.com` domains
 * `TELEGRAM_CHAT_ID` telegram chat id
 * `TELEGRAM_START_MESSAGE` telegram send message by pattern: <start message>+<domain>+<end message>+<datetimestamp>
 * `TELEGRAM_END_MESSAGE` telegram send message by pattern: <start message>+<domain>+<end message>+<datetimestamp>
 * `SLEEP_DELAY` delay per check each domain
 * `THREADS_N` number of threads
 * `RETRY_TIMES` how much TimeS, script retry connect to domain, before mark that domain as banned
 * `REQUEST_TIMEOUT` how much Time request wait for domain answer, before mark that domain as banned
 * `TIME_RECHECK` delay in seconds for rechecking domains list
