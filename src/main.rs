extern crate enet;

use std::net::Ipv4Addr;

use enet::*;

fn main() {
    let enet = Enet::new().expect("could not initialize Enet");
    let local_addr = Address::new(Ipv4Addr::LOCALHOST, 9001);
    let mut host = enet.create_host::<()>(
        Some(&local_addr), 
        2, 
        ChannelLimit::Limited(1), 
        BandwidthLimit::Unlimited, 
        BandwidthLimit::Unlimited)
        .expect("cloud not create host");
    
    loop {
        match host.service(1000).expect("service failed") {
            Some(Event::Connect(_)) => println!("new connection"),
            Some(Event::Disconnect(..)) => println!("disconnect"),
            Some(Event::Receive { 
                channel_id, 
                ref packet, 
                ..
            }) => println!(
                "got packet on channel {}, content: `{}`", 
                channel_id,
                std::str::from_utf8(packet.data()).unwrap()),
            _ => ()
        }
    }

}