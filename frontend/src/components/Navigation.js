import React, { useState }  from 'react'
import { AppBar, Toolbar, IconButton, Typography, Button, Drawer, List, ListItem, ListItemIcon, ListItemText } from '@material-ui/core';
import MenuIcon from '@material-ui/icons/Menu';
import HomeIcon from '@material-ui/icons/Home';
import "./Navigation.css"
import {Link} from "react-router-dom";

function Navigation() {
    const [openDrawer, setOpenDrawer] = useState(false);

    const toggleDrawer = (state) => (e) => {
        setOpenDrawer(state);
    };

    return (
        <div className="root">
            <AppBar position="static" color="transparent">
                <Toolbar>
                    <IconButton edge="start" color="inherit" onClick={toggleDrawer(true)} aria-label="menu">
                        <MenuIcon />
                    </IconButton>
                    <Drawer anchor="left" open={openDrawer} onClose={toggleDrawer(false)}>
                        <List className="list">
                            <ListItem button component={Link} to="/">
                                <ListItemIcon><HomeIcon /></ListItemIcon>
                                <ListItemText primary="Home" />
                            </ListItem>
                            
                        </List>
                    </Drawer>
                    <Typography variant="h6" className="root">
                        Loan tracker
                    </Typography>
                    <Button component={Link} to="/login" color="inherit">Login</Button>
                </Toolbar>
            </AppBar>
        </div>
    )
}

export default Navigation
