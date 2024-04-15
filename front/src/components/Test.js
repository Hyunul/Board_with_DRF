import { useState } from 'react'
import AxiosC from '../common/AxiosC'
import { removeCookie, setCookie } from '../common/Cookie'

export default function Test() {
    const [user, setUser] = useState({ email: '', password: '' })

    /** Get User Login Info */
    const onChange = async (event) => {
        const { name, value } = event.target
        setUser({
            ...user,
            [name]: value,
        })
    }

    /** Get Login Response from Server */
    const clickBtnLogin = async () => {
        const config = {
            method: 'post',
            url: 'http://localhost:8000/user/login/',
            data: user,
        }
        const { data } = await AxiosC(config)
        setCookie('accessToken', data.access)
    }

    /** Logout */
    const clickBtnLogout = async () => {
        removeCookie('accessToken')
    }

    return (
        <div>
            <input
                onChange={onChange}
                name="email"
                type="text"
                placeholder="Enter Ur Email"
            />
            <input
                onChange={onChange}
                name="password"
                type="password"
                placeholder="Enter Ur pw"
            />
            <button onClick={clickBtnLogin}>LOGIN</button>
            <button onClick={clickBtnLogout}>LOGOUT</button>
        </div>
    )
}