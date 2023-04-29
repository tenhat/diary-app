import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import apiClient from '../apiClient';

const DiaryList = () => {
  const [diaries, setDiaries] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await apiClient.get('/api/diaries');
      setDiaries(response.data);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>日記一覧</h1>
      <ul>
        {diaries.map((diary) => (
          <li key={diary.id}>
            <Link to={`/diaries/${diary.id}`}>{diary.title}</Link>
          </li>
        ))}
      </ul>
      <Link to="/diaries/new">新しい日記を作成</Link>
    </div>
  );
};

export default DiaryList;

