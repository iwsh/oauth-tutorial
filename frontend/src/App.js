import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import { useState, useEffect } from 'react';


function App() {
  const params = window.location.search;
  const backend_baseurl = process.env.REACT_APP_BACKEND_BASEURL
  const [message, setMessage] = useState("")
  const [username, setUsername] = useState("")
  const [avatar_url, setAvatarUrl] = useState("")
  const github_client_id = process.env.REACT_APP_GITHUB_CLIENT_ID
  const github_oauth_url = `https://github.com/login/oauth/authorize?client_id=${github_client_id}&scope=user:read`

  const code = params.startsWith('?code=') ? params.split('=')[1] : undefined;

  useEffect(() => {
    if (code && !message) {
      axios.post(backend_baseurl + '/login/oauth/github', {
        code: code
      }, {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      })
        .then(response => {
          console.log(response.data);
          setMessage(response.data.message);
          setUsername(response.data.username);
          setAvatarUrl(response.data.avatar_url);
        })
        .catch(error => {
          setMessage("Cannot login. Try Again.");
          console.log(error);
        });
    }
  })


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {
          message ?
            <div>
              <p>{message}</p>
            </div>
            : null
        }
        {
          username ?
            <div>
              <img src={avatar_url} alt="user_icon" height='100' />
              <p>Hello {username}.</p>
            </div>
            : null
        }
        <a
          className='App-link'
          href={github_oauth_url}
        >
          LOGIN with Github
        </a>
      </header>
    </div>
  );
}

export default App;
