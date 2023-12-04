import React from 'react'
import logo from '../assets/images/vaasagarKoodam.png'
import wave from '../assets/svgs/wave.svg'
import Homebooks from './home/HomeBooks'
import Breadcrumb from '../components/Breadcrumbs'

const Home = () => {
    return (
        <>
            {/* Intro */}
            <div>
                <div className='primary-bg py-5 position-relative'>
                    <div className='d-md-flex m-auto justify-content-around align-items-center'>
                        <div className=' text-center'>
                            <img src={logo} className='logo' alt="" />
                        </div>
                        <div className=''>
                            <div className=''>
                                <h1 className='text-light title_name fst-italic title-txt fw-bolder'>Vaasagar</h1>
                                <h1 className='text-light title_name fst-italic title-txt fw-bolder'>Koodam</h1>
                            </div>
                        </div>
                    </div>
                </div>
                <div className=''>
                    <img src={wave} className='' alt="" />
                </div>
            </div>
            {/* Welcome */}
            <div className='px-md-5'>
                <div className='py-md-5' >
                    <p className='welcome-para px-md-5 fst-italic text-style'>Welcome to Vaasagar Koodam, your literary sanctuary where stories unfold and knowledge blossoms. Immerse yourself in a world of enchanting tales and insightful narratives carefully curated for every reader. Explore the boundless realms of literature at Vaasagar Koodam, where every book is a journey waiting to be embarked upon. Unleash the magic of words and discover a symphony of stories at your fingertips.</p>
                </div>
                <Homebooks title={"Popular Books"} />
                <Homebooks title={"Trending Now"} />
                {/* Authors */}
                <div className='p-md-5'>
                    <h3 className='text-style fw-semibold'>Authors</h3>
                    <p className='welcome-para pt-3 fst-italic text-style'>Vaasagar Koodam empowers authors to share their literary creations with the world. Our user-friendly platform provides a seamless experience for writers to publish their books and connect with a diverse audience. Whether you're a seasoned author or a budding storyteller, Vaasagar Koodam offers a supportive space to showcase your work. Join us in fostering a vibrant community of writers and readers, where every story finds its place in the rich tapestry of literature.</p>
                </div>
            </div>
        </>
    )
}

export default Home
