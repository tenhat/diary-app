import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import UserList from './components/UserList';
import DiaryList from './components/DiaryList';
import DiaryForm from './components/DiaryForm';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Login} />
        <Route path="/register" component={Register} />
        <Route path="/users" component={UserList} />
        <Route path="/diaries" exact component={DiaryList} />
        <Route path="/diaries/new" component={DiaryForm} />
        <Route path="/diaries/:id" component={DiaryForm} />
      </Switch>
    </Router>
  );
}

export default App;
