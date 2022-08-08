import { Outlet, Link } from "react-router-dom";
import "./Layout.css"


const Layout = () => {
  return (
    <>
     <nav className="wrap_router">
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/blogs">Blog</Link>
          </li>
          <li>
            <Link to="/contact">Contact</Link>
          </li>
        </ul>
      </nav> 

      <Outlet />
    </>
  )
};

export default Layout;