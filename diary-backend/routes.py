from flask import request, jsonify
from app import app, db
from models import User, Diary, Tag

# ユーザー登録
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': 'ユーザー名はすでに登録されています。'}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'success': 'ユーザー登録が完了しました。'}), 201

# ユーザー認証
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({'error': 'ユーザー名またはパスワードが正しくありません。'}), 401

    return jsonify({'success': 'ログインに成功しました。'}), 200

# 日記の作成
@app.route('/api/diaries', methods=['POST'])
def create_diary():
    data = request.get_json()
    title = data['title']
    content = data['content']
    user_id = data['user_id']
    tags = data['tags']

    diary = Diary(title=title, content=content, user_id=user_id)
    for tag_name in tags:
        tag = Tag(name=tag_name)
        diary.tags.append(tag)

    db.session.add(diary)
    db.session.commit()

    return jsonify({'success': '日記が作成されました。'}), 201

# 日記の編集
@app.route('/api/diaries/<int:diary_id>', methods=['PUT'])
def update_diary(diary_id):
    diary = Diary.query.get(diary_id)
    if diary is None:
        return jsonify({'error': '日記が見つかりませんでした。'}), 404

    data = request.get_json()
    title = data['title']
    content = data['content']
    tags = data['tags']

    diary.title = title
    diary.content = content
    diary.tags = []
    for tag_name in tags:
        tag = Tag(name=tag_name)
        diary.tags.append(tag)

    db.session.commit()

    return jsonify({'success': '日記が更新されました。'}), 200

# 日記の削除
@app.route('/api/diaries/<int:diary_id>', methods=['DELETE'])
def delete_diary(diary_id):
    diary = Diary.query.get(diary_id)
    if diary is None:
        return jsonify({'error': '日記が見つかりませんでした。'}), 404

    db.session.delete(diary)
    db.session.commit()

    return jsonify({'success': '日記が削除されました。'}), 200

# 日記の取得
@app.route('/api/diaries', methods=['GET'])
def get_diaries():
    diaries = Diary.query.all()
    diaries_list = []

    for diary in diaries:
        diary_data = {
            'id': diary.id,
            'title': diary.title,
            'content': diary.content,
            'user_id': diary.user_id,
            'tags': [tag.name for tag in diary.tags]
        }
        diaries_list.append(diary_data)

    return jsonify(diaries_list), 200

# ユーザー一覧の取得
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = []

    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username
        }
        users_list.append(user_data)

    return jsonify(users_list), 200

# 特定のユーザーが作成した日記の取得
@app.route('/api/users/<int:user_id>/diaries', methods=['GET'])
def get_user_diaries(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'ユーザーが見つかりませんでした。'}), 404

    diaries = user.diaries.all()
    diaries_list = []

    for diary in diaries:
        diary_data = {
            'id': diary.id,
            'title': diary.title,
            'content': diary.content,
            'tags': [tag.name for tag in diary.tags]
        }
        diaries_list.append(diary_data)

    return jsonify(diaries_list), 200
