import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useHistory } from 'react-router-dom';
import apiClient from '../apiClient';

const DiaryForm = () => {
  const { id } = useParams();
  const history = useHistory();
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [tags, setTags] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      if (id) {
        const response = await apiClient.get(`/api/diaries/${id}`);
        setTitle(response.data.title);
        setContent(response.data.content);
        setTags(response.data.tags.join(', '));
      }
    };
    fetchData();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      if (id) {
        await apiClient.put(`/api/diaries/${id}`, {
          title,
          content,
          user_id: 1,  // user_idを追加
          tags: tags.split(',').map((tag) => tag.trim()),
        });
      } else {
        await apiClient.post('/api/diaries', {
          title,
          content,
          user_id: 1,  // user_idを追加
          tags: tags.split(',').map((tag) => tag.trim()),
        });
      }
      history.push('/diaries');
    } catch (error) {
      console.error(error);
    }
  };


  return (
    <div>
      <h1>{id ? '日記を編集' : '新しい日記を作成'}</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="タイトル"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          placeholder="内容"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <input
          type="text"
          placeholder="タグ (カンマ区切り)"
          value={tags}
          onChange={(e) => setTags(e.target.value)}
        />
        <button type="submit">{id ? '更新' : '作成'}</button>
      </form>
    </div>
  );
};

export default DiaryForm;
