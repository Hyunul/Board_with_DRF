import React from 'react'

const Signup = () => {
    return (
        <form>
            <input name='username' placeholder='username'></input>
            <input name='password1' placeholder='password1'></input>
            <input name='password2' placeholder='password2'></input>
            <button>회원가입</button>
        </form>
    )
}

export default Signup