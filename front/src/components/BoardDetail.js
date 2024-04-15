import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import Board from '../components/Board';

const BoardDetail = () => {
    const { id } = useParams(); // /board/:idx와 동일한 변수명으로 데이터를 꺼낼 수 있습니다.
    const [loading, setLoading] = useState(true);
    const [board, setBoard] = useState({});

    useEffect(() => {
        const getBoard = async () => {
            const resp = await (await axios.get(`http://localhost:8000/post/${id}/`)).data;
            console.log(resp)
            setBoard(resp);
            setLoading(false);
        };

        getBoard();
    }, [id]);

    return (
        <div>
            {loading ? (
                <h2>loading...</h2>
            ) : (

                <Board
                    id={board.id}
                    title={board.title}
                    contents={board.body}
                    created_date={board.created_date}
                />
            )}
        </div>
    );
};

export default BoardDetail;