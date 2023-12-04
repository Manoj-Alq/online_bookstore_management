import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

const Header = () => {
    const [isScrolled, setIsScrolled] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            setIsScrolled(window.scrollY > 50);
        };

        window.addEventListener('scroll', handleScroll);

        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);

    return (
        <div>
            <nav class={`navbar navbar-expand-lg header ${isScrolled ? 'opaque' : ''}`}>
                <div class="container-fluid">
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse p-3 " id="navbarSupportedContent">
                        <ul class="navbar-nav me-auto mb-2  mb-lg-0">
                            <li class="nav-item ">
                                <Link class="nav-link text-light text-style fw-semibold" aria-current="page" to={"/"}>Home</Link>
                            </li>
                            <li class="nav-item ">
                                <a class="nav-link text-light text-style fw-semibold" aria-current="page" href="#">Book</a>
                            </li>
                            <li class="nav-item ">
                                <a class="nav-link text-light text-style fw-semibold" aria-current="page" href="#">Author</a>
                            </li>
                            <li class="nav-item ">
                                <a class="nav-link text-light text-style fw-semibold" aria-current="page" href="#">About</a>
                            </li>
                        </ul>
                        <h5 className='text-light text-style fw-semibold'>
                            <Link className='text-decoration-none text-light' to={"/login"}>
                                Login
                            </Link>
                        </h5>
                    </div>
                </div>
            </nav>
        </div>
    )
}

export default Header
