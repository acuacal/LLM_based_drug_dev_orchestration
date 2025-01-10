#!/bin/bash

# 로그 파일 경로 설정
LOG_FILE="/var/log/user_management.log"

# 로그 함수
log_action() {
    echo "$(date): $1" >> "$LOG_FILE"
}

# root 권한 확인
if [ "$(id -u)" -ne 0 ]; then
    echo "이 스크립트는 root 권한으로 실행해야 합니다." >&2
    exit 1
fi

# 사용자 이름 입력 받기
read -p "생성할 사용자 이름을 입력하세요: " username

# 사용자 이름 유효성 검사
if [ -z "$username" ]; then
    echo "사용자 이름을 입력해야 합니다."
    exit 1
fi

# 사용자 존재 여부 확인
if id "$username" &>/dev/null; then
    echo "사용자 '$username'이(가) 이미 존재합니다."
    log_action "사용자 '$username' 생성 시도 실패: 이미 존재하는 사용자"
    exit 1
fi

# 사용자 생성
if useradd -m -s /bin/bash "$username"; then
    echo "사용자 '$username'이(가) 성공적으로 생성되었습니다."
    log_action "사용자 '$username' 생성 성공"
else
    echo "사용자 '$username' 생성 중 오류가 발생했습니다."
    log_action "사용자 '$username' 생성 실패"
    exit 1
fi

# 비밀번호 설정
passwd "$username"
log_action "사용자 '$username'의 비밀번호 설정"

# SSH 키 설정
mkdir -p /home/$username/.ssh
read -p "RunPod의 SSH 공개키를 입력하세요: " ssh_public_key
echo "$ssh_public_key" >> /home/$username/.ssh/authorized_keys
chmod 700 /home/$username/.ssh
chmod 600 /home/$username/.ssh/authorized_keys
chown -R $username:$username /home/$username/.ssh
log_action "사용자 '$username'의 SSH 키 설정 완료"

# sudo 권한 부여 (선택사항)
read -p "사용자에게 sudo 권한을 부여하시겠습니까? (y/n): " grant_sudo
if [ "$grant_sudo" = "y" ]; then
    if usermod -aG sudo "$username"; then
        echo "$username ALL=(ALL) ALL" >> /etc/sudoers
        echo "sudo 권한이 부여되었습니다."
        log_action "사용자 '$username'에게 sudo 권한 부여"
    else
        echo "sudo 권한 부여 중 오류가 발생했습니다."
        log_action "사용자 '$username'에게 sudo 권한 부여 실패"
    fi
fi

echo "사용자 생성 프로세스가 완료되었습니다."
log_action "사용자 '$username' 생성 프로세스 완료"
