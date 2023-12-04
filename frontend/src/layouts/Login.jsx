import React from 'react'
import { Link } from 'react-router-dom'
import Breadcrumb from '../components/Breadcrumbs'

const Login = () => {
    return (
        <>
            <div className='primary-bg '>
                <div className='loginpage d-flex align-items-center position-relative'>
                <div className='breadcrumb'>
                    <Breadcrumb />
                </div>
                    <div className='loginDiv  p-3'>
                        <h1 className='text-center text-light title-txt'>Login here</h1>
                        <form className='p-4 bg-light rounded-4 border border-dark border-3 shadow-lg'>
                            <div class="mb-3">
                                <label for="username " class="form-label fw-bold text-style">Username</label>
                                <input type="text" class="form-control border border-dark border-1 input" id="username" aria-describedby="username" />
                            </div>
                            <div class="mb-3">
                                <label for="exampleInputPassword1" class="form-label fw-bold text-style">Password</label>
                                <input type="password" class="form-control border border-dark border-1 input" id="exampleInputPassword1" />
                            </div>
                            <div className='d-flex justify-content-between'>
                                <button type="submit" class="btn btn-primary"><Link className='text-decoration-none text-light text-style fw-semibold'>Login</Link></button>
                                <button class="btn btn-secondary"><Link className='text-decoration-none text-light text-style fw-semibold' to={'/signup'}>Signup</Link></button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Login
