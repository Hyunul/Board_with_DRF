import React, { useEffect, useState } from 'react';
import axios from "axios";
import { Link } from "react-router-dom";

const BoardList = () => {
    const [boardList, setBoardList] = useState([]);

    const getBoardList = async () => {
        const resp = await (await axios.get('http://localhost:8000/post/')).data; // 2) 게시글 목록 데이터에 할당
        console.log(resp)
        setBoardList(resp); // 3) boardList 변수에 할당

    }

    useEffect(() => {
        getBoardList(); // 1) 게시글 목록 조회 함수 호출
    }, []);

    return (
        <div>
            <ul>
                {boardList && boardList.map((board) => (
                    <li key={board.id}>
                        <Link to={`/post/${board.id}/`}>{board.title}</Link>
                        <p>{board.body}</p>
                        <p>{board.created_date}</p>
                        <hr style={{ border: '1px solid #000' }} />
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default BoardList;