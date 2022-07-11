"""
A router has a number of so-called network interfaces or line cards, through which packets can enter and leave the router. In practically all cases, a packet leaves the router through another line card than it arrived on. It may well happen that during a very short time there arrive packets on several input line cards which need to go to the same output line card.

To deal with such sudden arrival bursts at an output line card, the line card contains a certain amount of buffer memory, in which packets are stored in first-come-first-served (FCFS) order. We also say that packets enter a queue. Whenever the line card wants to pick the next packet to transmit, it will inspect the queue and retrieve the head-of-queue packet for transmission.

In this setup, when a packet of yours arrives at its output line card, it may find a number of other packets ahead of itself in the queue, and all these other packets will be transmitted before your packet. The waiting time between entering the output line card and finishing the transmission of all previous packets is called the queueing delay. Note that the queueing delay is not controllable, it depends on how many packets (and for which destinations) others in the Internet generate.

Suppose the output line card has data rate R bps, and there are N packets ahead of yours in the queue, each of those has length L bits. What is the waiting time of your packet before its transmission starts? Please develop an expression and fill in the Python function below.
"""
def queueing_delay (rate_bps, numPackets, packetLength_b):
    trans = packetLength_b / rate_bps
    return numPackets * trans

print ("{:.3f}".format(queueing_delay(1000000, 7, 10000)))
print(queueing_delay(100*10**6, 20, 1500*8) * 1000)