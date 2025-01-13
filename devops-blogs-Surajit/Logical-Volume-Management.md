-> Logical Volume Management(LVM)
	-> Flexible Capacity
		-You can create file systems that extend across multiple devices.
		-You can agregate multiple storage devices into a single logical volume.
		-Expand or shrink file system in real-time while the data remains online and fully accessible.
		-Online Data relocation
			Easily migrate data from 1 storage device to another while online.
			
		-Increase throughput by allowing your system to read data in parallel.
		
		-Data redundancy/Data mirroring.
			Increase fault tolerance and reliablilty by having more than one copy of your data.
			
		-create point in time snapshots of ur filesystem.
		
		-File systems 
		4. Logical Volume(LV)
		3. Volume Groups(VG)
		2. Pysical Volumes(PV).
		1. Storage devices
		
		1. Command to check what all storage disks are available-
		lvmdiskscan
		lsblk
		lsblk -p
		df -hf
		fdisk -l
		
		2. create PV
		
		pvcreate /dev/sdb
		pvs //to check pv list
		
		3. create VG
		vg create vg_app /dev/sdb
		vgs //to check VG
		
		4. create Logical values
			lvcreate -L 20G -n lv_data vg_app
			lvs //to check VG
			lvdisplay
			
		5. Creating file system to the LV.
			mkfs -t ext4 /dev/vg_app/lv_data
			
		6. Creating Mount point.
		
			mkdir data
			mount /dev/vg_app/lv_data /data
			
			df -h /data
			
		7. Creating space to store actual app files for our app.
			lvcreate -L 5G -n lv_a vg_app
			
		8. Creating file system to the the app storage.
			mkfs -t ext4 /dev/vg_app/lv_app
			
		9. Creating a mount point for the app storage.
			mkdir app
			Note - we will create the entry in  /etc/fstab so that the mount point is create at boot time.
				vi /etc/fstab
					/dev/vg_app/lv_app /app ext4 default 0 0 
					mount /app  //Now, it will read the fstab file and create a mount point for us...
					
				df -h
				
		//to check how much space left, we can use below command - 
			vgs 
	
		-> logical extents:
			So there is yet another layer of abstraction that we haven't yet talked about and that is logical extents.
			Actually, it's two layers of abstraction. So each of our logical volumes is actually divided up into LE's, which stands for logical extents.
			Or if we look at it from the other direction, a collection of logical extents makes up a logical volume. This is how LVM allows us to expand or shrink a logical volume.
			The logical volume manager just changes the number of underlying logical extents for that logical volume.
			To view information about these logical extents, use the lvdisplay command.
			Just like an LV is divided into LE, a PV is divided into PEs which stand for physical extents.
			We can create a new volume with out remaning space lets say for logs -
			
			lvcreate -l 100%FREE -n lv_logs vg_app
			lvs
			vgs
			
			Now, we do not have any free space. So here 1st we need to extend our logical group and then the logical volume. So, we need to repeat our initial steps -
			
			1. kvmdiskscan
			2. pvcreate /dev/sdc
			3. vgextend vg_app /dev/sdc
				pvs			
			4. lvextend -L +5G -r /dev/vg_app/lv_data
				lvs
		
		Removing LV
			umount /secrets
			lvremove /dev/vg_safe/lv_secrets
			vgs
			vgreduce vg_safe /dev/sde
			pvs
			vgremove vg_safe
			vgs
			pvs
			pvremove /dev/sdd
			
	Moving data from 1 PV to other.		
	pvmove <source_pv> <destination_pv>
	
	vgreduce vg_app /dev/sdb
	
	pvremove /dev/sdb
	
	pvs
----------------------------------------------------------------------------------------------------------
