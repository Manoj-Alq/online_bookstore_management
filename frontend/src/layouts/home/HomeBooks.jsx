import React from 'react'
import arrow from '../../assets/svgs/right-arrow.svg'
import book1 from '../../assets/images/Book1.jpg'
import book2 from '../../assets/images/Book2.jpg'
import book3 from '../../assets/images/Book3.jpg'
import book4 from '../../assets/images/Book4.jpg'

const Homebooks = ({data,title}) => {
    return (
        <div className='px-5 py-4 overflow-x-hidden'>
            <div className='d-flex justify-content-between '>
                <div><h3 className='fw-semibold text-style'>{title}</h3></div>
                <div><img src={arrow} className='arrow' alt="" /></div>
            </div>
            <div className='d-md-flex gap-3'>
                <img src={book1} className='bookimg object-fit-cover rounded-4' alt="" />
                <img src={book2} className='bookimg object-fit-cover rounded-4' alt="" />
                <img src={book3} className='bookimg object-fit-cover rounded-4' alt="" />
                <img src={book4} className='bookimg object-fit-cover rounded-4' alt="" />
            </div>
        </div>
    )
}

export default Homebooks
