import { AppBar, Button, Container, TextField, Toolbar, Typography } from '@mui/material';
import React, { useState } from 'react';

function App() {
  const [value, setvalue] = useState(null);
  const [result, setresult] = useState(null);
  const handlerClick = () => {
    fetch("http://localhost:8000/translate", {
      method: "POST",
      mode: "cors",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ "sentence": value }),
    }).then(res => res.json())
      .then(data => { setresult(data.translation) })
      .catch(err => console.log(err));
  };
  return (<div>
    <Container maxWidth='lg'>
      <AppBar position='static' color='primary'>
        <Toolbar>
          <Typography variant='h6' component='div' sx={{ flexgrow: 1 }}>
            Pig Latin Translator
          </Typography>
        </Toolbar>
      </AppBar>
      <br />
      <Typography variant='body1' component='div'>
        Please enter the text you would like to translate.
      </Typography>
      <TextField multiline rows={5} variant='outlined' onChange={(event) => setvalue(event.target.value)} />
      <br />
      <Button variant='contained' color='primary' onClick={handlerClick}>Submit</Button>
      <Typography variant='body1' component='div'>
        Result : {result}
      </Typography>
    </Container>
  </div>);
}

export default App;