import React, { useState, useEffect } from 'react';
import axios from 'axios';
import apiClient from '../apiClient';

const UserList = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await apiClient.get('/api/users');
      setUsers(response.data);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>ユーザー一覧</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>{user.username}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;
